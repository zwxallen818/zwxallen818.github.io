#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/reference/global-app-points-mall/compare"
SKILL="/Users/allen/.agents/skills/messy-figma-responsive/scripts/capture-compare.sh"
bash "$SKILL" "file://$ROOT/index.html" 414 2489 "$OUT" 621

# Hot 区专用截图（Skill 默认 selector 未覆盖）
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
cd "$tmp"
npm init -y >/dev/null 2>&1
npm install playwright@1.49.0 --silent 2>&1 | tail -1
OUT_DIR="$OUT" URL="file://$ROOT/index.html" node <<'NODE'
const { chromium } = require('playwright');
const path = require('path');
const out = process.env.OUT_DIR;
const url = process.env.URL;
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 414, height: 2489 } });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  for (const [sel, name] of [
    ['#hot-block', 'impl-hot'],
    ['.hot-grid', 'impl-hot-grid'],
  ]) {
    const loc = page.locator(sel).first();
    if (await loc.count()) {
      await loc.screenshot({ path: path.join(out, name + '.png') });
    }
  }
  await browser.close();
})();
NODE
