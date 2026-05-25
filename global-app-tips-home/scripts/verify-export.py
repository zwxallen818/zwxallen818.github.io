#!/usr/bin/env python3
"""PNG 导出校验（Phase 2）。过小或全透明 → FAIL。"""
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("SKIP: pip install pillow")
    sys.exit(0)

MIN_BYTES = 200


def check(path: Path) -> str:
    if path.stat().st_size < MIN_BYTES:
        return "FAIL tiny file"
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    if w < 2 or h < 2:
        return "FAIL small dimensions"
    if im.getextrema()[3] == (0, 0):
        return "FAIL fully transparent"
    return "OK"


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "assets")
    files = sorted(root.glob("*.png"))
    if not files:
        print(f"No PNG in {root}")
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
