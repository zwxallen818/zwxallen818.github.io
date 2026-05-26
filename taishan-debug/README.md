# 泰山 w3 develop 调试包

**版本：260526.231707.287746**

![二维码](https://raw.githubusercontent.com/zwxallen818/zwxallen818.github.io/main/taishan-debug/qr-debug.png?v=260526231707)

| 方式 | 链接 |
|------|------|
| **页面** | https://zwxallen818.github.io/taishan-debug/ |
| **二维码直链** | https://raw.githubusercontent.com/zwxallen818/zwxallen818.github.io/main/taishan-debug/qr-debug.png?v=260526231707 |
| **短链** | http://d.9527.com/?name=w3&durl=https%3A%2F%2Ftest-app-package.oss-cn-hangzhou.aliyuncs.com%2Fw31779808627.zip |
| **ZIP** | https://test-app-package.oss-cn-hangzhou.aliyuncs.com/w31779808627.zip |

## 本版（Review 修复）

- 跳过蓝牙：不再设置 `winbotEnabled`，遥控 move 会提示「指令未发送至设备」
- `sendBluetoothDataWithResponse` 在跳过模式下立即返回，避免 15s 超时
- 跳过时不拉取 FFF6 / getInfo 序列

安装前请删除 App 内旧 w3 包。
