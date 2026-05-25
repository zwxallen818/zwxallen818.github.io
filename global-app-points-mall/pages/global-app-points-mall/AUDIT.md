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

- `1464:685` 分隔条 8px `#f5f5f5`
- `1464:686` 标题 24px
- `1464:658` / `671` 等推荐卡：当前用代表性商品图 + code 文案（AUD 价、покупк）

## 响应式

- 禁止 max-width:414
- 商品区 `grid` + `auto-fill`（≥640px）
