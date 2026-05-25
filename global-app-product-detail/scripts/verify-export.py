#!/usr/bin/env python3
"""PNG 导出校验：过小或近乎单色视为 FAIL（messy-figma-responsive Phase 2）"""
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("SKIP: Pillow not installed")
    sys.exit(0)

MIN_BYTES = 200


def check(path: Path) -> str:
    if path.stat().st_size < MIN_BYTES:
        return "FAIL tiny file"
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    if w < 2 or h < 2:
        return "FAIL small dimensions"
    # 全透明或全白视为空白导出
    extrema = im.getextrema()
    if extrema[3] == (0, 0):
        return "FAIL fully transparent"
    return "OK"


def main():
    root = Path(__file__).resolve().parents[1] / "assets"
    files = sorted(root.glob("*.png"))
    if not files:
        print("No PNG in assets/")
        sys.exit(1)
    failed = 0
    for f in files:
        status = check(f)
        print(f"{status}\t{f.name}")
        if status.startswith("FAIL"):
            failed += 1
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
