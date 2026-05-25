# Design tokens · API 实测（8031:1892）

| Token | 值 | 来源 node |
|-------|-----|-----------|
| `--evs-black` | `#253746` | 文案通用 |
| `--evs-blue` | `#3877f5` | 链接、选中框 |
| `--muted` | `#849cbc` | 副文案 |
| `--divider-section` | `#f5f5f5` | `8031:1959` 8px 分隔 |
| `--card-border` | `#ebebeb` | `8031:1905` 未选中 |
| `--card-radius` | `16px` | `8031:1902` / `1905` |
| `--gift-bg` | `rgba(198,210,233,0.14)` | `8031:2027` opacity 0.14 |
| `--promo-grad` | `21.32deg #f3d854→#ffb900` | `8031:2048` |
| `--promo-opacity` | `0.2` | `8031:2048` |
| `--promo-gold` | `#f7b500` | 促销文案 |
| `--bar-line` | `#eef1f5` | `I8031:1993;0:1781` |
| `--btn-add-bg` | `#ebf1fe` | `I8031:1993;0:1777` |
| `--btn-radius` | `25px` | 底栏按钮 |
| `--btn-buy-grad` | `#3f97ff → #346bf1` | `I8031:1993;0:1775` |
| 标题 28 / lh36 / w590 | Semibold | `8031:1900` |
| Section 20 / lh30 / w590 | Semibold | `8031:2020` |
| Section lg 24 / lh32 / w590 | Semibold | `8031:1901` |
| Tab 20 / lh30 | Active w590 / inactive w400 | `8031:2015` |
| Nav 图标热区 | **30×30** 统一（返回/购物车/客服） | `8031:1988` 子 INSTANCE |

## 切图 height 规则

Images API `scale=3` 导出时，`<img height>` **必须写 Figma 1x 逻辑高**（`absoluteBoundingBox`），不是 PNG 像素 ÷ 3 手算，更不能从别的节点抄（如浮动客服 36px）。
