# COMPARE · 11974:7723

视口 **414×1312**，对照目录 `reference/global-app-tips-home/compare/`。

| 区域 | 稿面 | 实现 | 估分 |
|------|------|------|------|
| 顶区 Tips+消息+促销 | ref-top | impl-top / impl-promo | ~88% |
| 分类 chips | ref-chips | impl-chips | ~90% |
| 瀑布流 | ref-feed | impl-feed | ~86% |
| 底栏 Tab | ref-tabbar | impl-tabbar | ~91% |
| 全页 | ref-full | impl-full | ~88% |

## 差异说明

- 促销条：稿面为单层合成，实现为底图 + 代码叠字，极端缩放下字重略有差。
- 瀑布流后四卡：封面为单图裁切，圆角顶区与稿面遮罩略有 1–2px 差。
- 未实现状态栏 / Home Indicator（与 Skill 一致）。

**综合还原度 ~88%**
