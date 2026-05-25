# 同宽对比 · 8031:1892

| 设计画布 W×H | **414 × 3776** |
|--------------|------------------|
| ref 来源 | `reference/global-app-product-detail/ref-full.png`（Images API scale=1） |
| 实现截图视口 | **414 × 3776**（`compare/impl-full.png`） |

## Phase 5.5 分区截图

| 区域 | 稿面 | 实现 | 文件 |
|------|------|------|------|
| 顶栏+Hero+标题 | crop y0–620 | scroll 0 | `compare/ref-top.png` / `impl-top.png` |
| Model Selection | crop y850–1320 | `#model-section` | `ref-model.png` / `impl-model.png` |
| Tabs | crop y1410–1500 | `.tabs` | `ref-tabs.png` / `impl-tabs.png` |
| 底栏 | `8031:1993` 导出 | `.bottom-bar` | `figma-bottom-bar.png` / `impl-bottom-bar.png` |

## 差异 → 修正记录

### 底栏 `8031:1993`

| 项目 | 稿面 API | 初版 | Skill 流程后 |
|------|----------|------|--------------|
| 交付形态 | 代码布局 | 整栏 PNG → 猜 CSS | API + 代码 |
| 圆角 | 25px | 9px | 25px |
| Buy Now | 渐变 `#3f97ff→#346bf1` | 纯色 | 渐变 |
| Add 底 | `#ebf1fe` | `#e8f0ff` | `#ebf1fe` |
| 顶线 | `#eef1f5` | `#e3e3e3` | `#eef1f5` |

**还原度：底栏 ~92%**

### Model 卡

| 项目 | 稿面 API | 初版 | 修正后 |
|------|----------|------|--------|
| 圆角 | 16px | 12px | 16px |
| 选中边框 | 1px `#3877f5` | 2px | 1px |
| 未选中 | 1px `#ebebeb` | `#e8edf5` | `#ebebeb` |
| 赠品区底 | `#c6d2e9` @14% | 近似 | `rgba(198,210,233,0.14)` |

**还原度：Model ~88%**

### 促销条 `8031:2048`

| 项目 | 稿面 | 初版 | 修正后 |
|------|------|------|--------|
| 条 opacity | 0.2（仅底） | 整层 0.92 | `::before` 0.2 |
| 高度 | 40px | min-height | 40px |

### Tabs `8031:2014`

| 项目 | 稿面 | 初版 | 修正后 |
|------|------|------|--------|
| 高度 | 78px | auto | 78px |
| 激活指示 | slice 33×4 | CSS 方块 | `tab-indicator.png` |
| 字重 | Active 590 / 其他 400 | 全 600 | 600 / 400 |

### 标题/章节字重

| 节点 | 稿 w590 | 修正 |
|------|---------|------|
| `8031:1900` | 28/36 Semibold | `--fw-semibold` |
| `8031:1901` | 24/32 Semibold | section--lg |
| `8031:2020` | 20/30 Semibold | section__title |

## 流程违规（已写入 Skill § 经验教训）

1. **跳过 Phase 5.5 即交付** — 导致底栏/卡片长期偏离。
2. **「代码化」未读 API** — 按钮圆角/渐变/边框猜错。
3. **组合 CTA 先整图再改代码** — 应一开始即代码 + API token。

## 全页还原度自评

| 区块 | % |
|------|---|
| 底栏 | 92 |
| Model | 88 |
| Tabs+顶区 | 85 |
| 功能长图区 | 82（插图 scale 差异） |
| **综合** | **~87%** |

未达 90% 主因：功能图导出比例与稿面裁切边界；下轮可对照 `ref-full` 微调 `feature__img` 圆角与间距。
