#!/usr/bin/env python3
"""
从 Figma nodes API 提取 tokens.json（Phase 4）。
用法: FIGMA_TOKEN=... python3 extract-tokens.py <fileKey> <id1,id2,...> [out.json]
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request

API = "https://api.figma.com/v1/files"


def hex_color(c: dict, opacity: float | None = None) -> str:
    r, g, b = int(c["r"] * 255), int(c["g"] * 255), int(c["b"] * 255)
    if opacity is not None and opacity < 1:
        return f"rgba({r},{g},{b},{opacity:.3f})"
    return f"#{r:02x}{g:02x}{b:02x}"


def parse_fill(fills: list | None, node_opacity: float | None) -> dict | None:
    if not fills:
        return None
    for f in fills:
        if not f.get("visible", True):
            continue
        op = (f.get("opacity", 1) or 1) * (node_opacity or 1)
        if f.get("type") == "SOLID":
            return {"type": "solid", "color": hex_color(f["color"], op if op < 1 else None)}
        if f.get("type") == "GRADIENT_LINEAR":
            stops = []
            for s in f.get("gradientStops", []):
                c = s["color"]
                stops.append(
                    {"color": hex_color(c), "position": s.get("position", 0)}
                )
            return {"type": "gradient", "stops": stops}
    return None


def walk(node: dict, out: list) -> None:
    bb = node.get("absoluteBoundingBox") or {}
    style = node.get("style") or {}
    entry = {
        "nodeId": node.get("id"),
        "name": node.get("name"),
        "type": node.get("type"),
        "bbox": {
            "w": round(bb.get("width", 0), 1),
            "h": round(bb.get("height", 0), 1),
        },
        "cornerRadius": node.get("cornerRadius"),
        "strokeWeight": node.get("strokeWeight"),
        "opacity": node.get("opacity"),
    }
    fill = parse_fill(node.get("fills"), node.get("opacity"))
    if fill:
        entry["fill"] = fill
    strokes = node.get("strokes") or []
    if strokes and node.get("strokeWeight"):
        for s in strokes:
            if s.get("type") == "SOLID" and s.get("visible", True):
                entry["stroke"] = hex_color(s["color"])
                break
    if style.get("fontSize"):
        entry["font"] = {
            "size": style.get("fontSize"),
            "weight": style.get("fontWeight"),
            "lineHeight": style.get("lineHeightPx"),
        }
    if node.get("characters"):
        entry["text"] = node["characters"]
    if any(
        k in entry
        for k in ("fill", "stroke", "font", "text", "cornerRadius")
        if entry.get(k) is not None
    ) or entry["bbox"]["w"] > 0:
        out.append(entry)
    for ch in node.get("children") or []:
        walk(ch, out)


def main() -> None:
    token = os.environ.get("FIGMA_TOKEN")
    if not token:
        print("FIGMA_TOKEN required", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) < 3:
        print(
            "Usage: extract-tokens.py <fileKey> <comma-separated-ids> [output.json]",
            file=sys.stderr,
        )
        sys.exit(1)
    file_key, ids = sys.argv[1], sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else "tokens.json"
    url = f"{API}/{file_key}/nodes?ids={ids}&depth=8"
    req = urllib.request.Request(url, headers={"X-Figma-Token": token})
    data = json.load(urllib.request.urlopen(req))
    tokens: list[dict] = []
    for wrap in data.get("nodes", {}).values():
        walk(wrap.get("document", {}), tokens)
    payload = {"fileKey": file_key, "ids": ids.split(","), "tokens": tokens}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(tokens)} entries → {out_path}")


if __name__ == "__main__":
    main()
