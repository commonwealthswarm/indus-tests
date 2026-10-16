"""Corpus loading. See docs/CORPUS_FORMAT.md."""
import json
from dataclasses import dataclass
from typing import List, Optional

TOP_FIELDS = ("source", "license", "sign_list", "inscriptions")
INSCRIPTION_FIELDS = ("id", "site", "signs")


@dataclass(frozen=True)
class Inscription:
    id: str
    site: Optional[str]
    signs: List[str]


@dataclass(frozen=True)
class Corpus:
    source: str
    license: str
    sign_list: str
    inscriptions: List[Inscription]


def load_corpus(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("corpus must be a JSON object")
    for name in TOP_FIELDS:
        if name not in data:
            raise ValueError("missing top-level field: %s" % name)
    inscriptions = []
    seen = set()
    for i, raw in enumerate(data["inscriptions"]):
        if not isinstance(raw, dict):
            raise ValueError("inscription %d is not an object" % i)
        for name in INSCRIPTION_FIELDS:
            if name not in raw:
                raise ValueError("inscription %d missing field: %s" % (i, name))
        if raw["id"] in seen:
            raise ValueError("duplicate inscription id: %s" % raw["id"])
        seen.add(raw["id"])
        if not raw["signs"]:
            raise ValueError("empty signs list in inscription %s" % raw["id"])
        inscriptions.append(
            Inscription(raw["id"], raw["site"], [str(s) for s in raw["signs"]]))
    return Corpus(data["source"], data["license"], data["sign_list"], inscriptions)
