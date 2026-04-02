from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from .utils import clean_text, load_json_file


def _dataset_node(obj: Any) -> Dict[str, Any]:
    """
    Locate the JSON-LD node that represents the dataset.

    Supports common shapes:
    - top-level object with "@type": "Dataset"
    - top-level object with "@graph": [ ... ]
    - top-level object with "@graph": { ... } (rare)
    """
    if isinstance(obj, dict):
        if obj.get("@type") == "Dataset":
            return obj
        graph = obj.get("@graph")
        if isinstance(graph, list):
            for node in graph:
                if isinstance(node, dict) and node.get("@type") == "Dataset":
                    return node
        if isinstance(graph, dict):
            if graph.get("@type") == "Dataset":
                return graph
    raise ValueError("Could not locate a schema.org node with @type == 'Dataset'.")


def _extract_creator(creator_value: Any) -> List[str]:
    if creator_value is None:
        return []
    if isinstance(creator_value, list):
        creators = []
        for item in creator_value:
            creators.extend(_extract_creator(item))
        return creators
    if isinstance(creator_value, dict):
        name = creator_value.get("name")
        return [str(name).strip()] if name else []
    return [str(creator_value).strip()]


def parse_schemaorg_jsonld(jsonld_path: str | Path) -> Dict[str, Any]:
    """
    Parse a small schema.org JSON-LD record into a Python dictionary.

    This teaching parser extracts a subset of fields useful for comparing metadata standards.
    """
    obj = load_json_file(jsonld_path)
    ds = _dataset_node(obj)

    name = ds.get("name")
    description = ds.get("description")
    creator_list = _extract_creator(ds.get("creator"))

    publisher_value = ds.get("publisher")
    publisher = None
    if isinstance(publisher_value, dict):
        publisher = publisher_value.get("name")
    elif publisher_value is not None:
        publisher = publisher_value

    identifier = ds.get("identifier")
    keywords = ds.get("keywords") or []
    if isinstance(keywords, str):
        keywords_list = [keywords]
    else:
        keywords_list = [str(k).strip() for k in keywords if str(k).strip()]

    license_url = ds.get("license")

    # Try to extract a format from distributions (if present)
    format_ = None
    distributions = ds.get("distribution")
    if isinstance(distributions, list) and distributions:
        first = distributions[0]
        if isinstance(first, dict):
            format_ = first.get("encodingFormat")
    elif isinstance(distributions, dict):
        format_ = distributions.get("encodingFormat")

    return {
        "standard": "schema.org",
        "title": clean_text(name or ""),
        "creator": [c for c in creator_list if c],
        "publisher": clean_text(str(publisher or "") or ""),
        "identifier": clean_text(str(identifier or "") or ""),
        "description": clean_text(str(description or "") or ""),
        "keywords": keywords_list,
        "license": clean_text(str(license_url or "") or ""),
        "format": clean_text(str(format_ or "") or ""),
        "type": ds.get("@type"),
    }

