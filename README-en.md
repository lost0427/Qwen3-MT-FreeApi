<div align="center">

# 🌐 Qwen3-MT-FreeApi

[🇨🇳 中文版](README.md) | [🇺🇸 English](README-en.md)

</div>

A lightweight local proxy service that allows you to use the **Qwen3-MT multilingual translation model** just like calling OpenAI. It is compatible with the OpenAI `/v1/chat/completions` interface, ready-to-use, and supports mutual translations among up to **92 languages + auto (automatic detection of input language)**.

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

## 🗣️ How to Specify Translation Language

When calling the interface, specify the translation language through the `model` parameter.

This service supports translations among multiple languages. Translations between languages are mainly achieved by specifying the corresponding model name, for example:

- `qwen3-mt-zh-en`: Chinese → English
- `qwen3-mt-en-zh`: English → Chinese

See the "Language Reference Table" below for supported language codes.

| English Name        | Language Code   |
| ---------- | ------ |
| English         | en     |
| Simplified Chinese       | zh     |
| Traditional Chinese       | zh\_tw |
| Russian         | ru     |
| Japanese         | ja     |
| Korean         | ko     |
| Spanish         | es     |
| French         | fr     |
| Portuguese       | pt     |
| German         | de     |
| Italian         | it     |
| Thai         | th     |
| Vietnamese        | vi     |
| Indonesian       | id     |
| Malay         | ms     |
| Arabic         | ar     |
| Hindi         | hi     |
| Hebrew         | he     |
| Burmese         | my     |
| Tamil         | ta     |
| Urdu         | ur     |
| Bengali         | bn     |
| Polish         | pl     |
| Dutch         | nl     |
| Romanian        | ro     |
| Turkish         | tr     |
| Khmer         | km     |
| Lao         | lo     |
| Cantonese       | yue    |
| Czech         | cs     |
| Greek         | el     |
| Swedish         | sv     |
| Hungarian       | hu     |
| Danish         | da     |
| Finnish         | fi     |
| Ukrainian       | uk     |
| Bulgarian       | bg     |
| Serbian         | sr     |
| Telugu         | te     |
| Afrikaans       | af     |
| Armenian        | hy     |
| Assamese        | as     |
| Asturian        | ast    |
| Basque         | eu     |
| Belarusian       | be     |
| Bosnian         | bs     |
| Catalan         | ca     |
| Cebuano        | ceb    |
| Croatian        | hr     |
| Egyptian Arabic    | arz    |
| Estonian        | et     |
| Galician        | gl     |
| Georgian        | ka     |
| Gujarati        | gu     |
| Icelandic        | is     |
| Javanese        | jv     |
| Kannada        | kn     |
| Kazakh         | kk     |
| Latvian        | lv     |
| Lithuanian       | lt     |
| Luxembourgish      | lb     |
| Macedonian       | mk     |
| Maithili        | mai    |
| Maltese        | mt     |
| Marathi        | mr     |
| Mesopotamian Arabic | acm    |
| Moroccan Arabic    | ary    |
| Najdi Arabic       | ars    |
| Nepali         | ne     |
| North Azerbaijani    | az     |
| North Levantine Arabic | apc    |
| North Uzbek        | uz     |
| Norwegian Bokmål     | nb     |
| Norwegian Nynorsk    | nn     |
| Occitan        | oc     |
| Oriya         | or     |
| Pangasinan        | pag    |
| Sicilian        | scn    |
| Sindhi         | sd     |
| Sinhala        | si     |
| Slovak         | sk     |
| Slovenian        | sl     |
| South Levantine Arabic | ajp    |
| Swahili        | sw     |
| Tagalog        | tl     |
| Ta'iz-Mukalla Arabic | acq    |
| Tosk Albanian      | sq     |
| Tunisian Arabic    | aeb    |
| Venetian        | vec    |
| Waray-Waray       | war    |
| Welsh         | cy     |
| Persian         | fa     |
| Auto-detect Input Language | auto   |

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
