from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import xml.etree.ElementTree as ET

from .utils import clean_text, local_name, normalize_list, parse_xml_file


def parse_datacite_xml(xml_path: str | Path) -> Dict[str, Any]:
    """
    Parse a small DataCite XML record into a Python dictionary.

    This is a teaching parser. It extracts a subset of commonly taught fields.
    """
    root = parse_xml_file(xml_path)

    def first_text(local: str) -> str | None:
        for el in root.iter():
            if local_name(el.tag) == local:
                txt = (el.text or "").strip()
                if txt:
                    return txt
        return None

    def texts(local: str) -> List[str]:
        out: List[str] = []
        for el in root.iter():
            if local_name(el.tag) != local:
                continue
            txt = (el.text or "").strip()
            if txt:
                out.append(txt)
        return out

    # Identifier: prefer DOI-type if available
    doi_identifier = None
    any_identifier = None
    for el in root.iter():
        if local_name(el.tag) != "identifier":
            continue
        txt = (el.text or "").strip()
        if not txt:
            continue
        if any_identifier is None:
            any_identifier = txt
        if el.attrib.get("identifierType") == "DOI":
            doi_identifier = txt
    identifier = doi_identifier or any_identifier

    creators = []
    for el in root.iter():
        if local_name(el.tag) == "creatorName":
            txt = (el.text or "").strip()
            if txt:
                creators.append(txt)

    title = first_text("title")
    publisher = first_text("publisher")
    publication_year = first_text("publicationYear")

    resource_type_general = None
    for el in root.iter():
        if local_name(el.tag) == "resourceType" and el.attrib.get("resourceTypeGeneral"):
            resource_type_general = el.attrib.get("resourceTypeGeneral")
            break
        # Some DataCite examples may use a separate element
        if local_name(el.tag) == "resourceTypeGeneral":
            txt = (el.text or "").strip()
            if txt:
                resource_type_general = txt
                break

    description = None
    for el in root.iter():
        if local_name(el.tag) != "description":
            continue
        # Prefer Abstract when available
        if el.attrib.get("descriptionType") in (None, "Abstract"):
            txt = (el.text or "").strip()
            if txt:
                description = txt
                if el.attrib.get("descriptionType") == "Abstract":
                    break
    return {
        "standard": "DataCite",
        "title": clean_text(title or ""),
        "creator": creators,
        "publisher": clean_text(publisher or ""),
        "identifier": clean_text(identifier or ""),
        "publicationYear": clean_text(publication_year or "") or None,
        "resourceTypeGeneral": clean_text(resource_type_general or ""),
        "description": clean_text(description or ""),
    }

