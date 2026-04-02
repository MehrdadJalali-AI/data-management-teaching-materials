from __future__ import annotations

from typing import Any, Dict, List, Tuple


def _has_nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, list):
        return any(str(v).strip() for v in value)
    return bool(str(value).strip())


def completeness_checks(metadata: Dict[str, Any]) -> List[Tuple[str, bool]]:
    """
    Teaching/demo completeness checks.

    This is not a formal validator; it provides simple “does this field exist?”
    feedback aligned with Week 1 learning goals.
    """
    checks = [
        ("title", _has_nonempty(metadata.get("title"))),
        ("creator", _has_nonempty(metadata.get("creator"))),
        ("identifier", _has_nonempty(metadata.get("identifier"))),
        ("description", _has_nonempty(metadata.get("description"))),
        (
            "publisher_or_year",
            _has_nonempty(metadata.get("publisher")) or _has_nonempty(metadata.get("publicationYear")) or _has_nonempty(metadata.get("date")),
        ),
    ]
    return checks


def completeness_score(metadata: Dict[str, Any]) -> Dict[str, Any]:
    checks = completeness_checks(metadata)
    total = len(checks)
    passed = sum(1 for _, ok in checks if ok)
    score = round((passed / total) * 100, 1)
    return {"standard": metadata.get("standard"), "score_percent": score, "checks": checks}

