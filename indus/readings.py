"""Proposed decipherment ("reading") loading. See docs/READINGS_FORMAT.md."""
import json
import os
from dataclasses import dataclass, field
from typing import Dict, List, Union

REQUIRED_FIELDS = ("name", "author", "year", "citation", "sign_list", "language", "values")
STRING_FIELDS = ("name", "author", "citation", "sign_list", "language")


@dataclass(frozen=True)
class Reading:
    name: str
    author: str
    year: int
    citation: str
    sign_list: str
    language: str
    values: Dict[str, Union[str, List[str]]]
    lexicon: List[str] = field(default_factory=list)
    notes: str = ""


def _fail(path, problem):
    raise ValueError("%s: %s" % (os.path.basename(path), problem))


def _valid_value(v):
    if isinstance(v, str):
        return v != ""
    if isinstance(v, list):
        return len(v) > 0 and all(isinstance(x, str) and x != "" for x in v)
    return False


def load_reading(path):
    with open(path, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            _fail(path, "invalid JSON: %s" % e)
    if not isinstance(data, dict):
        _fail(path, "reading must be a JSON object")
    for name in REQUIRED_FIELDS:
        if name not in data:
            _fail(path, "missing required field: %s" % name)
    for name in STRING_FIELDS:
        if not isinstance(data[name], str):
            _fail(path, "%s must be a string" % name)
    if isinstance(data["year"], bool) or not isinstance(data["year"], int):
        _fail(path, "year must be an int")
    values = data["values"]
    if not isinstance(values, dict) or not values:
        _fail(path, "empty values: map at least one sign")
    for sign, v in values.items():
        if not _valid_value(v):
            _fail(path, "bad value for sign %s: must be a non-empty string "
                        "or a non-empty list of non-empty strings" % sign)
    lexicon = data.get("lexicon", [])
    if not isinstance(lexicon, list) or not all(isinstance(w, str) and w for w in lexicon):
        _fail(path, "lexicon must be a list of non-empty strings")
    notes = data.get("notes", "")
    if not isinstance(notes, str):
        _fail(path, "notes must be a string")
    return Reading(data["name"], data["author"], data["year"], data["citation"],
                   data["sign_list"], data["language"], dict(values), list(lexicon), notes)


def load_readings(directory):
    names = sorted(n for n in os.listdir(directory) if n.endswith(".json"))
    return [load_reading(os.path.join(directory, n)) for n in names]
