# AUDIT · 11974:7723

- **fileKey**: `Q1tcc8nYpjqViTXz6kx1ED`
- **frame**: 首页吸顶 · 414×1312
- **ref**: `reference/global-app-tips-home/ref-full.png`

## 跳过

| 节点 | 原因 |
|------|------|
| 11974:7828 状态栏 | Skill：不实现系统状态栏 |
| 11974:7841 Home Indicator | Skill：不实现 Home 条 |
| 11974:7842 Group 3 | `hidden="true"` |
| 11974:7733 分隔线 | `hidden="true"` |

## layoutRole 决策

- **顶栏**：`cluster-lr` — 禁止整栏导航 PNG；消息图标右对齐 `ml-auto`。
- **促销条**：有标题/正文/箭头 → **代码文案** + 背景切图，非整栏 PNG 按钮。
- **分类**：横向滚动 chips → 纯 CSS。
- **底栏**：四 Tab 有中文标签 → **代码** + 单图标 PNG（34px 槽位）。
- **feed 上两卡**：组件实例复杂遮罩 → **整卡 PNG**；其余 **图+meta 代码**。

## 风险

- 分类轨宽 622px，需 `overflow-x` 露出「技术科普」「使用技巧」。
- `feed-*.png` 原图偏大，容器 `width:100%` 约束列宽 184px 逻辑宽。
