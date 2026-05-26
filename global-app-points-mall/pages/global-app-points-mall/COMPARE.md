# COMPARE · 1464:396

视口 **414×2489**；宽屏 **621×2489**（`compare/wide/`）。

## Phase 5.5 截图（2026-05-19）

| 稿面 | 实现 |
|------|------|
| `compare/ref-hot.png` | `compare/impl-hot.png`（`#hot-block`：灰条+标题+四卡） |
| `compare/ref-hot.png`（裁切 hot 区） | `compare/impl-hot-grid.png`（仅 grid） |
| `compare/ref-hero.png` … | `compare/impl-full.png` |

生成命令：

```bash
python3 scripts/crop-ref.py reference/global-app-points-mall/ref-full.png \
  pages/global-app-points-mall/blocks-crops.json reference/global-app-points-mall/compare
bash scripts/capture-compare.sh
```

## Hot Recommendation 修复说明

- 左列卡 `1464:638/648` 的 Save/AUD/价格/按钮在稿面为**帧级兄弟节点**，整卡 PNG 会漏字 → 改为 **商品图 slice + code 文案**。
- 间距按 API 元数据：卡 **180×343**、列距 **14px**、行距 **16px**、沟 **20px**；标题 x=**18**，标题下距首行卡 **33px**。
- 二次对齐（差异表）：标题 `min-height:44` + `width:160`；卡固定高；Save 省略号；AUD `top:3px`；按钮 **160×32** 固定 `margin-top:7px`；左列图 `object-position: top`。

## 估分

| 区域 | 估分 |
|------|------|
| 顶区 Oval+积分+通知 | ~90% |
| Banner+筛选 | ~88% |
| 商品 grid（代表性整卡 PNG） | ~87% |
| Hot Recommendation（impl-hot 像素粗估 ~75%） | ~85% 目视 |
| 宽屏铺满 | ~91% |

**综合 ~88%**（Hot 区字体渲染/按钮底色渐变仍会有像素差）
