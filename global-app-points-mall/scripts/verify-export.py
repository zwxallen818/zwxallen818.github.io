#!/usr/bin/env python3
"""PNG 导出校验（Phase 2）。过小、全透明、Tab 图标裁切条 → FAIL。"""
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("SKIP: pip install pillow")
    sys.exit(0)

MIN_BYTES = 200
# Tab 类图标若宽高比过小，多为误导子图层（如 58×27）
TAB_ICON_MIN_ASPECT = 0.65


def check(path: Path) -> str:
    if path.stat().st_size < MIN_BYTES:
        return "FAIL tiny file"
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    if w < 2 or h < 2:
        return "FAIL small dimensions"
    if im.getextrema()[3] == (0, 0):
        return "FAIL fully transparent"
    name = path.name.lower()
    if "tab-icon" in name or name.startswith("tab-"):
        if h > 0 and (w / h) < TAB_ICON_MIN_ASPECT:
            return (
                f"FAIL tab aspect {w}x{h} — use INSTANCE root nodeId, not I…;0:xxx"
            )
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
