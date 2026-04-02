from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


def local_name(tag: str) -> str:
    """Return the XML local name (strip any namespace prefix/URI)."""
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _first_text_by_local_name(
    root: ET.Element, target_local_name: str, *, attrib_predicate: Optional[dict] = None
) -> Optional[str]:
    for el in root.iter():
        if local_name(el.tag) != target_local_name:
            continue
        if attrib_predicate:
            ok = True
            for k, v in attrib_predicate.items():
                if el.attrib.get(k) != v:
                    ok = False
                    break
            if not ok:
                continue
        txt = (el.text or "").strip()
        if txt:
            return txt
    return None


def _texts_by_local_name(root: ET.Element, target_local_name: str) -> List[str]:
    out: List[str] = []
    for el in root.iter():
        if local_name(el.tag) != target_local_name:
            continue
        txt = (el.text or "").strip()
        if txt:
            out.append(txt)
    return out


def parse_xml_file(xml_path: str | Path) -> ET.Element:
    """Parse an XML file using only the Python standard library."""
    xml_path = Path(xml_path)
    tree = ET.parse(xml_path)
    return tree.getroot()


def load_json_file(json_path: str | Path) -> Any:
    json_path = Path(json_path)
    return json.loads(json_path.read_text(encoding="utf-8"))


def normalize_list(value: Any) -> List[str]:
    """Normalize a field that may be a string, list, or None into a list[str]."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    s = str(value).strip()
    return [s] if s else []


_ws_re = re.compile(r"\s+")


def clean_text(s: str) -> str:
    """Normalize whitespace for readable output."""
    s = s or ""
    s = _ws_re.sub(" ", s).strip()
    return s

