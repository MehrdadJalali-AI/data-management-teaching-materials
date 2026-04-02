from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET
from typing import Any, Dict, List

from .utils import clean_text, local_name, parse_xml_file, _first_text_by_local_name, _texts_by_local_name, normalize_list


def parse_dublin_core_xml(xml_path: str | Path) -> Dict[str, Any]:
    """
    Parse a small Dublin Core (DC) XML record into a Python dictionary.

    This is a *teaching* parser: it uses local-name matching (namespace-agnostic)
    and extracts a beginner-friendly subset of fields.
    """
    root = parse_xml_file(xml_path)

    def first(name: str) -> str | None:
        return _first_text_by_local_name(root, name)

    title = clean_text(first("title") or "")
    publisher = clean_text(first("publisher") or "")
    identifier = clean_text(first("identifier") or "")
    date = clean_text(first("date") or "")
    format_ = clean_text(first("format") or "")

    # Dublin Core typically uses creator as a repeatable element
    creators: List[str] = normalize_list(_texts_by_local_name(root, "creator"))

    # Description may appear as dcterms:description or dc:description
    description = clean_text(first("description") or "")

    subject = normalize_list(_texts_by_local_name(root, "subject"))

    # If the XML uses dc:description inside dcterms:description, the local-name is still "description".
    return {
        "standard": "Dublin Core",
        "title": title or None,
        "creator": creators,
        "publisher": publisher or None,
        "identifier": identifier or None,
        "description": description or None,
        "subject": subject,
        "date": date or None,
        "format": format_ or None,
    }

