# BLOCKS · 1464:398 Oval

画布 **414×273**（装饰顶区，非整页）。背景 `#f3f6fa` 为演示页衬托。

| # | 区块 | nodeId | layoutRole | wideScreenRule | 实现 |
|---|------|--------|------------|----------------|------|
| 1 | Oval 装饰 | 1464:398 | full-bleed | `width:100%` 拉满；`object-fit:cover` top | slice `oval-header.png` |
| 2 | 演示顶栏 | — | cluster-lr | 沟内 `marginX=20`；右占位 `ml-auto` | code 占位 |

## 说明

-  BOOLEAN + mask 复杂曲线 → **整帧 export**，不用 CSS 近似。
- 无 Status Bar / Tab / 文案在稿内。
- 可叠用于 Tips 等页顶区（替换原 178px header-gradient 时须对照产品稿）。
