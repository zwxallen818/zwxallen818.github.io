# ASSETS — 割草序列浮层 (3792:35591)

## 画布

- 帧：`3792:35591`「割草序列浮层」390×844
- 参考图：`reference/ref-full.png`

## 上次图标错误原因（根因）

| 问题 | 错误做法 | 正确做法 |
|------|----------|----------|
| 时间轴圆点 | 全部用 CSS 圆或同一枚勾选图 | **完成**用 `3792:35602` 导出；**进行中**用 `3792:35608`；**当前区**用 `3792:35704` 双椭圆 |
| 参数 chip 图标 | 手写 SVG / 通用 icon 库 | 按 nodeId 导出：`Component 11/12`（割草机+速度线）、`Group 1000010228`（距离）、`icon_obstacle` |
| Laps chip | 导出 `Group 1000010251` 里纯白底矩形 | 稿面仅为灰底 pill + 文案，**无独立图标**，用 CSS `#f3f6f8` 圆角底 |
| 关闭按钮 | 箭头/back 类图标 | `3792:35596` `back_icon` 实为 **X 关闭** |
| 充电座 | 误用风机/电源类图标 | `3792:35620` `icon_充电座` |
| 机器人位置 | 未导出或错图 | `3792:35642` `Icons/20/deebot-扫地` |
| 勿导出 | `Rectangle 3468086/8087/8088` 单独 PNG | 仅为 chip 背景，会得到**空白图** |

## 资源清单（本地 `assets/`）

| 文件 | Figma nodeId | 用途 | 显示高度 |
|------|--------------|------|----------|
| `icon-close.png` | 3792:35596 | 右上关闭 | 24px |
| `icon-done-complete.png` | 3792:35602 | 已完成步骤勾选 | 16px |
| `icon-done-progress.png` | 3792:35608 | 进行中步骤（青绿环） | 16px |
| `timeline-dot-outer.png` | 3792:35705 | 当前区时间轴外圈 | 12px |
| `timeline-dot-inner.png` | 3792:35706 | 当前区时间轴内圈 | 8px |
| `icon-charging-station.png` | 3792:35620 | Finish 充电座 | 24px |
| `icon-speed-mower.png` | 3792:35650 | 速度 chip（Component 11） | 30px |
| `icon-speed-mower-active.png` | 3792:35675 | 当前区速度 chip（Component 12） | 30px |
| `icon-distance.png` | 3792:35654 | 10cm 距离 | 30px |
| `icon-obstacle.png` | 3792:35658 | 避障 | 30px |
| `icon-robot.png` | 3792:35642 | 地图上机器人 | 30px |
| `btn-ok.png` | 3792:35597 | 底栏 OK 按钮整组 | 52px |

## 用代码实现（非切图）

- 遮罩 `3792:35594`：`rgba(0,0,0,0.6)`
- 底 sheet 白底 + 顶圆角 24px
- 时间轴竖线 `Rectangle 599x`：2px `#C3CDD8`
- Skip：`3792:35643/35645` 描边圆角 pill
- Laps / 速度文案 chip 背景：`#F3F6F8`，圆角 8px
- Status Bar / Home Indicator：**不实现**
