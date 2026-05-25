#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMPARE="$ROOT/reference/global-app-tips-home/compare"
PAGE="file://$ROOT/index.html"
W=414
H=1312

mkdir -p "$COMPARE"
python3 "$(dirname "$0")/crop-ref.py" \
  "$ROOT/reference/global-app-tips-home/ref-full.png" \
  "$ROOT/pages/global-app-tips-home/blocks-crops.json" \
  "$COMPARE"

TMP=$(mktemp -d)
cd "$TMP"
npm init -y >/dev/null 2>&1
npm install playwright@1.49.0 --silent

node <<NODE
const { chromium } = require('playwright');
const path = require('path');
const out = '$COMPARE';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: $W, height: $H } });
  await page.goto('$PAGE', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(out, 'impl-full.png'), fullPage: true });
  await page.locator('.top-bar').screenshot({ path: path.join(out, 'impl-top.png') });
  await page.locator('.promo').screenshot({ path: path.join(out, 'impl-promo.png') });
  await page.locator('.chips').screenshot({ path: path.join(out, 'impl-chips.png') });
  await page.locator('.feed').screenshot({ path: path.join(out, 'impl-feed.png') });
  await page.locator('.tab-bar').screenshot({ path: path.join(out, 'impl-tabbar.png') });
  await browser.close();
})();
NODE

echo "compare shots in $COMPARE"
