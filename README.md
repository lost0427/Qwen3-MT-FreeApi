<div align="center">

# 🌐 Qwen3-MT-FreeApi

[🇨🇳 中文版](README.md) | [🇺🇸 English](README-en.md)

</div>


一个轻量级本地代理服务，让你像调用 OpenAI 一样使用 **Qwen3-MT 多语言翻译模型**。兼容 OpenAI `/v1/chat/completions` 接口，开箱即用，支持中英互译。

---

## ✨ 特性

- ✅ 兼容 OpenAI 接口格式：`/v1/chat/completions`
- 🔄 支持 **中文 ↔ 英文** 自动翻译
- 🔐 API Key 认证保护
- 🧩 自动识别翻译方向（通过 `model` 参数）
- 🖥️ 提供一键安装与启动脚本（Windows）

---

## 🚀 快速开始（Windows 用户推荐）

### 1. 安装依赖（使用 Anaconda）

确保已安装 [Anaconda](https://www.anaconda.com/) 并将其路径添加到系统环境变量。

```bash
install-q3mt.bat
```

### 2. 启动服务

运行启动脚本：

```bash
start-q3mt.bat
```

---

## 🔐 配置 API Key

编辑 `.env` 文件，设置你的密钥：

```env
API_KEY=your-secret-api-key-here
```

---

## 📦 项目结构

```
Qwen3-MT-FreeApi/
│
├── .env.example          # API_KEY 示例文件
├── .gitignore            # Git 忽略规则
├── install-q3mt.bat      # 一键安装脚本（Windows）
├── main.py               # 核心服务代码
├── requirements.txt      # Python 依赖
└── start-q3mt.bat        # 一键启动脚本（Windows）
```

---

## ⚙️ 注意事项

- 确保已安装 **Anaconda** 并加入系统环境变量。
- 第一次使用前请运行 `install-q3mt.bat` 仅需一次。
- `.env` 文件中的 `API_KEY` 需与请求头一致。
- 本服务依赖 Qwen3-MT 在线模型接口，需保持网络畅通。

---

## 📄 许可证

MIT License
