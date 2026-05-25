/**
 * 8031:1892 · 切图判定（messy-figma-responsive Phase 2）
 * 每行：nodeId / slice|code|skip / 理由
 */
export const pageMarginX = "16px";
export const canvas = { width: 414, height: 3776 };

export const sliceManifest = [
  { nodeId: "8031:2048", kind: "code", reason: "渐变促销条 + 文案" },
  { nodeId: "8031:1988", kind: "slice", file: "nav-bar.png", reason: "返回/购物车/客服组合" },
  { nodeId: "8031:1896", kind: "slice", file: "hero-product.png", reason: "主产品图" },
  { nodeId: "8031:1898", kind: "slice", file: "carousel-dots.png", reason: "轮播指示" },
  { nodeId: "8031:1900", kind: "code", reason: "标题文案" },
  { nodeId: "8031:1902", kind: "code", reason: "Model 选中卡边框/圆角" },
  { nodeId: "8031:2033", kind: "slice", file: "gift-thumb.png", reason: "赠品缩略图" },
  { nodeId: "8031:2017", kind: "slice", file: "tab-indicator.png", reason: "Features 下划线" },
  { nodeId: "8031:1919", kind: "slice", file: "feature-effortless.png", reason: "功能图 1" },
  { nodeId: "8031:1954", kind: "slice", file: "feature-suction.png", reason: "功能图 2" },
  { nodeId: "8031:1924", kind: "slice", file: "feature-mopping.png", reason: "功能图 3" },
  { nodeId: "8031:1992", kind: "slice", file: "payment-icons.png", reason: "支付方式条" },
  { nodeId: "8031:2056", kind: "slice", file: "icon-arrow-right.png", reason: "积分行箭头" },
  { nodeId: "8031:1993", kind: "code", reason: "底栏：价格+双按钮，API 渐变/圆角 25" },
  { nodeId: "8031:2024", kind: "skip", reason: "Status Bar" },
  { nodeId: "8031:1994", kind: "skip", reason: "Home Indicator" },
] as const;
