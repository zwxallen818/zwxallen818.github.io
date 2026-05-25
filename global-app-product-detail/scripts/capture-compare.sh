#!/usr/bin/env bash
# Phase 5.5：414×3776 视口截取实现图（需 npx playwright）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMPARE="$ROOT/reference/global-app-product-detail/compare"
PAGE="file://$ROOT/index.html"
W=414
H=3776

TMP=$(mktemp -d)
cd "$TMP"
npm init -y >/dev/null 2>&1
npm install playwright@1.49.0 --silent

node <<NODE
const { chromium } = require('playwright');
const path = require('path');
const out = '$COMPARE';
const pageUrl = '$PAGE';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: $W, height: $H } });
  await page.goto(pageUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(out, 'impl-full.png'), fullPage: true });
  await page.locator('.promo-strip').screenshot({ path: path.join(out, 'impl-top-promo.png') });
  await page.locator('#model-section').screenshot({ path: path.join(out, 'impl-model.png') });
  await page.locator('.tabs').screenshot({ path: path.join(out, 'impl-tabs.png') });
  await page.locator('.bottom-bar').screenshot({ path: path.join(out, 'impl-bottom-bar.png') });
  await browser.close();
})();
NODE

python3 <<PY
from PIL import Image
ref = Image.open('$ROOT/reference/global-app-product-detail/ref-full.png')
cmp = '$COMPARE'
for name, box in [
    ('ref-top.png', (0, 0, 414, 620)),
    ('ref-model.png', (0, 850, 414, 1320)),
    ('ref-tabs.png', (0, 1410, 414, 1500)),
]:
    ref.crop(box).save(f'{cmp}/{name}')
print('crops ok')
PY

echo "compare shots in $COMPARE"
