"""Reproducibility manifests for test-bench results.

A manifest is a JSON object that records where a set of counts came from,
so the result can be re-verified later:

- ``source_paths`` / ``source_sha256``: the source or input file(s).
- ``corpus_path`` / ``corpus_sha256``: the corpus JSON, hashed in canonical
  form (sorted keys, no extra whitespace, UTF-8).
- ``code_paths`` / ``code_sha256``: the counting code files, by path.
- ``semantics``: the declared count semantics, checked against
  ``SUPPORTED_SEMANTICS``.
- ``counts_path`` / ``counts_sha256``: the counts output, hashed in the same
  canonical form as the corpus.

Paths are relative to the manifest's directory unless absolute. Several
files are combined into one hash over ``path NUL sha256 LF`` lines in the
order listed, so renaming or reordering a file also changes the hash.

Command line::

    python3 -m indus.manifest check MANIFEST.json
    python3 -m indus.manifest build --source S --corpus C --code F [--code F ...] \\
        --counts OUT.json --semantics key=value [...] --out MANIFEST.json

``check`` exits 0 when everything matches and 1 otherwise, printing each
problem on its own line.
"""

import argparse
import hashlib
import json
import os
import sys

MANIFEST_VERSION = 1

# Each semantics key and the values the test bench supports for it.
SUPPORTED_SEMANTICS = {
    "sequence_matches": ["overlapping", "non_overlapping"],
    "sequence_texts": ["distinct_inscriptions"],
    "denominator": ["nonzero_tokens", "all_tokens"],
    "zero_tokens": ["excluded", "included"],
}

# Pairs of (key, value) that cannot be declared together.
CONTRADICTORY_SEMANTICS = [
    (("denominator", "nonzero_tokens"), ("zero_tokens", "included")),
    (("denominator", "all_tokens"), ("zero_tokens", "excluded")),
]

REQUIRED_FIELDS = [
    "manifest_version",
    "source_paths",
    "source_sha256",
    "corpus_path",
    "corpus_sha256",
    "code_paths",
    "code_sha256",
    "semantics",
    "counts_path",
    "counts_sha256",
]


def canonical_json_bytes(obj):
    """Serialize obj as JSON with sorted keys, no extra whitespace, UTF-8."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as f:
        return sha256_bytes(f.read())


def sha256_canonical_json_file(path):
    with open(path, "rb") as f:
        obj = json.loads(f.read().decode("utf-8"))
    return sha256_bytes(canonical_json_bytes(obj))


def sha256_files(paths, base_dir="."):
    """One hash over several files, in the order listed."""
    h = hashlib.sha256()
    for p in paths:
        digest = sha256_file(_resolve(p, base_dir))
        h.update(p.encode("utf-8") + b"\0" + digest.encode("ascii") + b"\n")
    return h.hexdigest()


def _resolve(path, base_dir):
    return path if os.path.isabs(path) else os.path.join(base_dir, path)


def check_semantics(semantics):
    """Return a list of problems with a declared semantics mapping."""
    if not isinstance(semantics, dict):
        return ["semantics: must be an object"]
    problems = []
    for key in sorted(semantics):
        if key not in SUPPORTED_SEMANTICS:
            problems.append("semantics: unsupported key %r" % key)
        elif semantics[key] not in SUPPORTED_SEMANTICS[key]:
            problems.append("semantics: unsupported value %r for %r (supported: %s)"
                            % (semantics[key], key,
                               ", ".join(SUPPORTED_SEMANTICS[key])))
    for key in sorted(SUPPORTED_SEMANTICS):
        if key not in semantics:
            problems.append("semantics: missing key %r" % key)
    for (k1, v1), (k2, v2) in CONTRADICTORY_SEMANTICS:
        if semantics.get(k1) == v1 and semantics.get(k2) == v2:
            problems.append("semantics: contradictory %s=%s with %s=%s"
                            % (k1, v1, k2, v2))
    return problems


def compute_hashes(manifest, base_dir="."):
    """Recompute the four hashes named by the manifest's paths."""
    return {
        "source_sha256": sha256_files(manifest["source_paths"], base_dir),
        "corpus_sha256": sha256_canonical_json_file(
            _resolve(manifest["corpus_path"], base_dir)),
        "code_sha256": sha256_files(manifest["code_paths"], base_dir),
        "counts_sha256": sha256_canonical_json_file(
            _resolve(manifest["counts_path"], base_dir)),
    }


def build_manifest(source_paths, corpus_path, code_paths, counts_path,
                   semantics, base_dir="."):
    """Build a manifest dict for files that exist now."""
    manifest = {
        "manifest_version": MANIFEST_VERSION,
        "source_paths": list(source_paths),
        "corpus_path": corpus_path,
        "code_paths": list(code_paths),
        "counts_path": counts_path,
        "semantics": dict(semantics),
    }
    manifest.update(compute_hashes(manifest, base_dir))
    return manifest


def check_manifest(manifest, base_dir="."):
    """Return a list of problems; an empty list means everything matches."""
    if not isinstance(manifest, dict):
        return ["manifest: must be a JSON object"]
    problems = ["missing field: %s" % f for f in REQUIRED_FIELDS
                if f not in manifest]
    if problems:
        return problems
    if manifest["manifest_version"] != MANIFEST_VERSION:
        problems.append("manifest_version: unsupported %r"
                        % (manifest["manifest_version"],))
    problems.extend(check_semantics(manifest["semantics"]))
    checks = [
        ("source_sha256", lambda: sha256_files(manifest["source_paths"], base_dir)),
        ("corpus_sha256", lambda: sha256_canonical_json_file(
            _resolve(manifest["corpus_path"], base_dir))),
        ("code_sha256", lambda: sha256_files(manifest["code_paths"], base_dir)),
        ("counts_sha256", lambda: sha256_canonical_json_file(
            _resolve(manifest["counts_path"], base_dir))),
    ]
    for field, compute in checks:
        try:
            actual = compute()
        except (OSError, ValueError, TypeError) as e:
            problems.append("%s: cannot compute (%s)" % (field, e))
            continue
        if actual != manifest[field]:
            problems.append("%s mismatch: manifest %s, recomputed %s"
                            % (field, manifest[field], actual))
    return problems


def check_manifest_file(path):
    """Load a manifest file and check it relative to its own directory."""
    try:
        with open(path, "rb") as f:
            manifest = json.loads(f.read().decode("utf-8"))
    except (OSError, ValueError) as e:
        return ["manifest: cannot read %s (%s)" % (path, e)]
    return check_manifest(manifest, os.path.dirname(os.path.abspath(path)))


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python3 -m indus.manifest")
    sub = parser.add_subparsers(dest="cmd")
    p_check = sub.add_parser("check", help="verify a manifest")
    p_check.add_argument("manifest")
    p_build = sub.add_parser("build", help="write a manifest")
    p_build.add_argument("--source", action="append", required=True)
    p_build.add_argument("--corpus", required=True)
    p_build.add_argument("--code", action="append", required=True)
    p_build.add_argument("--counts", required=True)
    p_build.add_argument("--semantics", action="append", default=[],
                         metavar="KEY=VALUE")
    p_build.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    if args.cmd == "check":
        problems = check_manifest_file(args.manifest)
        for p in problems:
            print(p)
        if not problems:
            print("OK: all hashes and semantics match")
        return 1 if problems else 0
    if args.cmd == "build":
        semantics = dict(s.split("=", 1) for s in args.semantics)
        problems = check_semantics(semantics)
        if problems:
            for p in problems:
                print(p)
            return 1
        base_dir = os.path.dirname(os.path.abspath(args.out))
        rel = lambda p: os.path.relpath(os.path.abspath(p), base_dir)
        manifest = build_manifest([rel(p) for p in args.source], rel(args.corpus),
                                  [rel(p) for p in args.code], rel(args.counts),
                                  semantics, base_dir)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, sort_keys=True)
            f.write("\n")
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
