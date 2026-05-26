# AUDIT · 1464:396

- **frame**: 积分中心首页 · 414×2489
- **skip**: 1464:409 Status Bar

## 切图策略

| 类型 | 处理 |
|------|------|
| Oval / Banner / 复杂商品卡 | INSTANCE/FRAME export PNG |
| 返回、积分币、VIP 徽章、筛选箭头、勾选 | INSTANCE 根，height= bbox |
| 通知文案、筛选字、价格字 | **code** |
| 商品卡内俄文/英文标题 | 整卡 PNG 保留（避免漏字） |

## Hot Recommendation（帧底部）

- `1464:685` 分隔条 · code
- `1464:686` 标题 · code
- 四卡 **整卡 export**（scale=2）：`1464:638` → `hot-card-1.png` … `1464:671` → `hot-card-4.png`
- **禁止** 复用积分兑换区 `product-card-*.png`

## 响应式

- 禁止 max-width:414
- 商品区 `grid` + `auto-fill`（≥640px）
