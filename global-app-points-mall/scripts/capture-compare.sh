#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="/Users/allen/.agents/skills/messy-figma-responsive/scripts/capture-compare.sh"
bash "$SKILL" "file://$ROOT/index.html" 414 2489 \
  "$ROOT/reference/global-app-points-mall/compare" 621
