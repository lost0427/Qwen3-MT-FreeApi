<div align="center">

# 🌐 Qwen3-MT-FreeApi

[🇨🇳 中文版](README.md) | [🇺🇸 English](README-en.md)

</div>


一个轻量级本地代理服务，让你像调用 OpenAI 一样使用 **Qwen3-MT 多语言翻译模型**。兼容 OpenAI `/v1/chat/completions` 接口，开箱即用，支持多达 **92种语言 + auto（自动检测输入语言）** 的互相翻译。

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

## 🗣️ 如何指定翻译语言

调用接口时，通过 `model` 参数来指定翻译语言。  

本服务支持多种语言互译，语言间翻译主要通过指定对应的模型名称实现，例如：

- `qwen3-mt-zh-en`：中文 → 英文  
- `qwen3-mt-en-zh`：英文 → 中文  

支持的语言代码见下方“语言对照表”

| 中文名        | 语言代码   |
| ---------- | ------ |
| 英语         | en     |
| 简体中文       | zh     |
| 繁体中文       | zh\_tw |
| 俄语         | ru     |
| 日语         | ja     |
| 韩语         | ko     |
| 西班牙语       | es     |
| 法语         | fr     |
| 葡萄牙语       | pt     |
| 德语         | de     |
| 意大利语       | it     |
| 泰语         | th     |
| 越南语        | vi     |
| 印度尼西亚语     | id     |
| 马来语        | ms     |
| 阿拉伯语       | ar     |
| 印地语        | hi     |
| 希伯来语       | he     |
| 缅甸语        | my     |
| 泰米尔语       | ta     |
| 乌尔都语       | ur     |
| 孟加拉语       | bn     |
| 波兰语        | pl     |
| 荷兰语        | nl     |
| 罗马尼亚语      | ro     |
| 土耳其语       | tr     |
| 高棉语        | km     |
| 老挝语        | lo     |
| 粤语         | yue    |
| 捷克语        | cs     |
| 希腊语        | el     |
| 瑞典语        | sv     |
| 匈牙利语       | hu     |
| 丹麦语        | da     |
| 芬兰语        | fi     |
| 乌克兰语       | uk     |
| 保加利亚语      | bg     |
| 塞尔维亚语      | sr     |
| 泰卢固语       | te     |
| 南非荷兰语      | af     |
| 亚美尼亚语      | hy     |
| 阿萨姆语       | as     |
| 阿斯图里亚斯语    | ast    |
| 巴斯克语       | eu     |
| 白俄罗斯语      | be     |
| 波斯尼亚语      | bs     |
| 加泰罗尼亚语     | ca     |
| 宿务语        | ceb    |
| 克罗地亚语      | hr     |
| 埃及阿拉伯语     | arz    |
| 爱沙尼亚语      | et     |
| 加利西亚语      | gl     |
| 格鲁吉亚语      | ka     |
| 古吉拉特语      | gu     |
| 冰岛语        | is     |
| 爪哇语        | jv     |
| 卡纳达语       | kn     |
| 哈萨克语       | kk     |
| 拉脱维亚语      | lv     |
| 立陶宛语       | lt     |
| 卢森堡语       | lb     |
| 马其顿语       | mk     |
| 马加希语       | mai    |
| 马耳他语       | mt     |
| 马拉地语       | mr     |
| 美索不达米亚阿拉伯语 | acm    |
| 摩洛哥阿拉伯语    | ary    |
| 内志阿拉伯语     | ars    |
| 尼泊尔语       | ne     |
| 北阿塞拜疆语     | az     |
| 北黎凡特阿拉伯语   | apc    |
| 北乌兹别克语     | uz     |
| 书面语挪威语     | nb     |
| 新挪威语       | nn     |
| 奥克语        | oc     |
| 奥里亚语       | or     |
| 邦阿西楠语      | pag    |
| 西西里语       | scn    |
| 信德语        | sd     |
| 僧伽罗语       | si     |
| 斯洛伐克语      | sk     |
| 斯洛文尼亚语     | sl     |
| 南黎凡特阿拉伯语   | ajp    |
| 斯瓦希里语      | sw     |
| 他加禄语       | tl     |
| 塔伊兹-亚丁阿拉伯语 | acq    |
| 托斯克阿尔巴尼亚语  | sq     |
| 突尼斯阿拉伯语    | aeb    |
| 威尼斯语       | vec    |
| 瓦莱语        | war    |
| 威尔士语       | cy     |
| 西波斯语       | fa     |
| 自动检测输入语言   | auto   |

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
