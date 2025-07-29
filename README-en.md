<div align="center">

# 🌐 Qwen3-MT-FreeApi

[🇨🇳 中文版](README.md) | [🇺🇸 English](README-en.md)

</div>

A lightweight local proxy service that allows you to use the **Qwen3-MT multilingual translation model** just like calling OpenAI. Compatible with the OpenAI `/v1/chat/completions` interface, ready-to-use out of the box, supporting Chinese-English bidirectional translation.

---

## ✨ Features

- ✅ Compatible with OpenAI interface format: `/v1/chat/completions`
- 🔄 Supports **Chinese ↔ English** automatic translation
- 🔐 API Key authentication protection
- 🧩 Automatically identifies translation direction (via the `model` parameter)
- 🖥️ Provides one-click installation and startup scripts (for Windows)

---

## 🚀 Quick Start (Recommended for Windows Users)

### 1. Install Dependencies (Using Anaconda)

Make sure you have [Anaconda](https://www.anaconda.com/) installed and added to your system environment variables.

```bash
install-q3mt.bat
```

### 2. Start the Service

Run the startup script:
```bash
start-q3mt.bat
```

---

## 🔐 Configure API Key

Edit the `.env` file and set your secret key:

```env
API_KEY=your-secret-api-key-here
```

---

## 📦 Project Structure

```
Qwen3-MT-FreeApi/
│
├── .env.example          # API_KEY example file
├── .gitignore            # Git ignore rules
├── install-q3mt.bat      # One-click installation script (Windows)
├── main.py               # Core service code
├── requirements.txt      # Python dependencies
└── start-q3mt.bat        # One-click startup script (Windows)
```

---

## ⚙️ Notes

- Ensure **Anaconda** is installed and added to your system environment variables.
- Run `install-q3mt.bat` only once before first use.
- The `API_KEY` in the `.env` file must match the one in your request headers.
- This service relies on the online Qwen3-MT model interface; ensure stable internet connectivity.

---

## 📄 License

MIT License
