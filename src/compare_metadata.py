from __future__ import annotations

from typing import Any, Dict, List
import pandas as pd


def _join_creators(creators: Any) -> str:
    if creators is None:
        return ""
    if isinstance(creators, list):
        return "; ".join([str(c).strip() for c in creators if str(c).strip()])
    return str(creators).strip()


def to_comparison_row(meta: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "standard": meta.get("standard"),
        "title": meta.get("title") or "",
        "creator": _join_creators(meta.get("creator")),
        "identifier": meta.get("identifier") or "",
        "description": (meta.get("description") or "").strip(),
        "publisher": meta.get("publisher") or "",
        "date_or_year": meta.get("publicationYear") or meta.get("date") or "",
        "format": meta.get("format") or "",
        "resourceType": meta.get("resourceTypeGeneral") or meta.get("resourceType") or "",
    }


def compare_three_standards(
    dublin_core: Dict[str, Any],
    datacite: Dict[str, Any],
    schemaorg: Dict[str, Any],
) -> pd.DataFrame:
    """
    Create a simple comparison table across the three standards.
    """
    rows: List[Dict[str, Any]] = [to_comparison_row(dublin_core), to_comparison_row(datacite), to_comparison_row(schemaorg)]
    df = pd.DataFrame(rows)
    return df

