# 泰山 w3 develop 调试包

**版本：260526.221856.287745**

![二维码](https://raw.githubusercontent.com/zwxallen818/zwxallen818.github.io/main/taishan-debug/qr-debug.png?v=260526221856)

| 方式 | 链接 |
|------|------|
| **页面** | https://zwxallen818.github.io/taishan-debug/ |
| **二维码直链** | https://raw.githubusercontent.com/zwxallen818/zwxallen818.github.io/main/taishan-debug/qr-debug.png?v=260526221856 |
| **短链** | http://d.9527.com/?name=w3&durl=https%3A%2F%2Ftest-app-package.oss-cn-hangzhou.aliyuncs.com%2Fw31779805136.zip |
| **ZIP** | https://test-app-package.oss-cn-hangzhou.aliyuncs.com/w31779805136.zip |

## 本版

- 开启「跳过蓝牙」后：`sendBluetoothData` **不再走原生**，仅记 `[SkipGate][BT_SEND]` 日志
- 同时 **取消** 扫描 30s / 连接 30s / 后台重连，避免稍后弹出蓝牙超时或离线弹窗

安装前请删除 App 内旧 w3 包。
