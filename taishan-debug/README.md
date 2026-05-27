# 泰山 w3 develop 调试包

**版本：260527.085149.287729**

## 国内 OSS（推荐）

| 方式 | 链接 |
|------|------|
| **安装页** | https://test-app-package.oss-cn-hangzhou.aliyuncs.com/taishan-debug/index.html |
| **二维码** | https://test-app-package.oss-cn-hangzhou.aliyuncs.com/taishan-debug/qr-debug.png?v=260527085149287729 |
| **ZIP** | https://test-app-package.oss-cn-hangzhou.aliyuncs.com/w3_260527.085149.287729_Debug.zip |
| **短链** | http://d.9527.com/?name=w3&durl=https%3A%2F%2Ftest-app-package.oss-cn-hangzhou.aliyuncs.com%2Fw3_260527.085149.287729_Debug.zip |

## 本版要点

- 真机必须 `initCentalManager`，不再伪造 `winbotEnabled`
- 遥控返回：断开蓝牙 + 回原生设备列表
- 加载完成后进 `/winbot`（不再 debug 直跳遥控）

安装前请删除 App 内旧 w3 包。
