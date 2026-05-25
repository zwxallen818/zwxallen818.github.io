#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="/Users/allen/.agents/skills/messy-figma-responsive/scripts/capture-compare.sh"
chmod +x "$SKILL" 2>/dev/null || true
bash "$SKILL" "file://$ROOT/index.html" 414 800 \
  "$ROOT/reference/global-app-header-oval/compare" 621
