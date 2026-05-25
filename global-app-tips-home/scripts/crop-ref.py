#!/usr/bin/env python3
"""
从 ref-full.png 按 BLOCKS 裁切稿面分区（Phase 5.5）。
用法: python3 crop-ref.py ref-full.png blocks-crops.json compare/
blocks-crops.json: [{"name":"top","y0":0,"y1":620}, ...]
"""
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("pip install pillow", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: crop-ref.py <ref-full.png> <crops.json> <out-dir>")
        sys.exit(1)
    ref = Image.open(sys.argv[1])
    crops = json.load(open(sys.argv[2], encoding="utf-8"))
    out_dir = Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)
    w = ref.width
    for c in crops:
        y0, y1 = int(c["y0"]), int(c["y1"])
        name = c["name"]
        box = (0, max(0, y0), w, min(ref.height, y1))
        ref.crop(box).save(out_dir / f"ref-{name}.png")
        print("ok", name, box[3] - box[1], "px h")
    print("done", out_dir)


if __name__ == "__main__":
    main()
