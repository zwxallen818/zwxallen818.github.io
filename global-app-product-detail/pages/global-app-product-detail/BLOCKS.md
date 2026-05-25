# BLOCKS · 8031:1892

**内容沟** `mx = 16px`（382px 内容宽 @414）· **禁止** `max-width` 锁死画布

| # | 区块 | 布局 | 切图 / 代码 |
|---|------|------|-------------|
| 1 | 促销条 `8031:2048` | flex 行，高 40px，渐变底 opacity 0.2 | code |
| 2 | 导航 `8031:1988` | 全宽，高 55px | slice `nav-bar.png` |
| 3 | Hero `8031:1893` | 全宽，产品图 + 轮播点 | slice hero + dots |
| 4 | 标题区 | 内容沟，圆角顶 20px 叠在 hero 上 | code 文案 |
| 5 | Promotions `8031:2018` | 内容沟 section | code |
| 6 | Model Selection | 内容沟；选中卡 cr16 蓝框 1px | code + gift 区 opacity 0.14 |
| 7 | Tabs `8031:2014` | 全宽 sticky，高 78px | code + slice 指示条 |
| 8 | Features | 内容沟/全宽图 | slice 三张 lifestyle |
| 9 | Commodity Parameters | 内容沟表格 | code |
| 10 | Pay | 内容沟 | slice 支付图标条 |
| 11 | 底栏 `8031:1993` | fixed，414×111 grid | **code**（价格+双按钮） |

## 跨块契约

- 全宽：促销条、导航、Hero、Tabs、底栏。
- 分隔：`#f5f5f5` 8px 条（`8031:1959`）用于 Model 上方向分隔。
