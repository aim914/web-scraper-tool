# 🔥 Web Scraper + Video Download Tool

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     __        _______ ____  ___    ____ _____ _   _ ______   ║
║     \ \      / / ____/ ___||__ \  / ___|_   _| | | |  _ \  ║
║      \ \ /\ / /|  _| \___ \ / / | |     | | | | | | | | | ║
║       \ V  V / | |___ ___) / /_ | |___  | | | |_| | |_| | ║
║        \_/\_/  |_____|____/____| \____| |_|  \___/|____/  ║
║                                                              ║
║            + VIDEO DOWNLOADER + AUTO DETECT                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt-dlp-red?style=for-the-badge&logo=youtube&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📸 Features Preview

```
┌─────────────────────────────────────────────────┐
│           📋 MAIN MENU                          │
├─────────────────────────────────────────────────┤
│                                                 │
│   1.  🔍 Web Search                             │
│   2.  🔎 Website Keyword Search                 │
│   3.  🔗 Website Link Search                    │
│                                                 │
│   4.  📝 Text Scrape                            │
│   5.  🔗 Links Scrape                           │
│   6.  🖼️  Images Scrape                         │
│                                                 │
│   7.  🎬 Video Download                         │
│   8.  📥 File Download                          │
│   9.  🖼️  Download All Images                   │
│                                                 │
│   10. 🚪 Exit                                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Supported Platforms

| Platform | Video | Reels | Shorts | Status |
|----------|:-----:|:-----:|:------:|:------:|
| 📸 Instagram | ✅ | ✅ | - | 🟢 Working |
| 🎵 TikTok | ✅ | ✅ | - | 🟢 Working |
| ▶️ YouTube | ✅ | - | ✅ | 🟢 Working |
| 🐦 Twitter/X | ✅ | - | - | 🟢 Working |
| 👤 Facebook | ✅ | - | - | 🟢 Working |
| 🔴 Reddit | ✅ | - | - | 🟢 Working |
| 🌐 Any Site | ✅ | - | - | 🟢 Working |

---

## 📁 Supported File Formats

```
┌──────────────────────────────────────────────────────┐
│  🖼️  IMAGES          │  🎬 VIDEOS        │  🎵 AUDIO │
│  ├─ JPG              │  ├─ MP4           │  ├─ MP3   │
│  ├─ PNG              │  ├─ WebM          │  ├─ WAV   │
│  ├─ GIF              │  ├─ MKV           │  ├─ OGG   │
│  ├─ WebP             │  ├─ AVI           │  ├─ FLAC  │
│  └─ SVG              │  └─ MOV           │  └─ M4A   │
│                       │                   │           │
│  📄 DOCUMENTS        │  📦 ARCHIVES      │  🔧 OTHER │
│  ├─ PDF              │  ├─ ZIP           │  ├─ APK   │
│  ├─ DOC/DOCX         │  ├─ RAR           │  ├─ EXE   │
│  ├─ XLS/XLSX         │  ├─ 7Z            │  ├─ TXT   │
│  └─ PPT              │  └─ TAR/GZ        │  └─ JSON  │
└──────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Start

### 1️⃣ Clone Repository
```bash
git clone https://github.com/aim914/web-scraper-tool.git
cd web-scraper-tool
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Tool
```bash
python web_scraper.py
```

---

## 🎬 Video Download Examples

### Download Instagram Reel
```
┌─────────────────────────────────────────────────┐
│  🎬 VIDEO DOWNLOAD                              │
│  ─────────────────────────────────────────────  │
│  Instagram | TikTok | YouTube | Twitter         │
│                                                 │
│  Paste video link: https://instagram.com/reel/..│
│                                                 │
│  Quality choose karo:                           │
│  1. Best (original quality)                     │
│  2. 720p (HD)                                   │
│  3. 480p (SD)                                   │
│  4. 360p (Low)                                  │
│                                                 │
│  Select (1-4): 2                                │
│                                                 │
│  ✓ Downloaded: video.mp4 (5.2 MB)               │
└─────────────────────────────────────────────────┘
```

### Web Search
```
┌─────────────────────────────────────────────────┐
│  🔍 WEB SEARCH                                  │
│  ─────────────────────────────────────────────  │
│  Search: python tutorial                         │
│                                                 │
│  📋 10 Results: "python tutorial"               │
│                                                 │
│  1. Python Tutorial for Beginners               │
│     https://example.com/python                   │
│     Learn Python from scratch...                │
│                                                 │
│  2. Advanced Python Programming                 │
│     https://example.com/advanced                 │
│     Master Python concepts...                   │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Installation Guide

### Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git ffmpeg
pip install -r requirements.txt
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg
pip3 install -r requirements.txt
```

### macOS
```bash
brew install python ffmpeg
pip3 install -r requirements.txt
```

### Windows
```powershell
winget install Python.FFmpeg
pip install -r requirements.txt
```

---

## 📂 Save Location

All downloads are saved to:
```
/storage/emulated/0/only for work/downloads/
```

---

## 🎨 Terminal Preview

```
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     🔍 SEARCH    📥 DOWNLOAD    🎬 VIDEOS            ║
    ║                                                      ║
    ║     Instagram | TikTok | YouTube | Twitter           ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝

    📋 MAIN MENU
    ─────────────────────────────────────────
    1.  🔍 Web Search
    2.  🔎 Website Keyword Search
    3.  🔗 Website Link Search
    4.  📝 Text Scrape
    5.  🔗 Links Scrape
    6.  🖼️  Images Scrape
    7.  🎬 Video Download
    8.  📥 File Download
    9.  🖼️  Download All Images
    10. 🚪 Exit

    Select (1-10): 7

    🎬 VIDEO DOWNLOAD
    ═══════════════════════════════════════════
    URL: https://instagram.com/reel/ABC123/
    Quality: best

    ⠹ Trying format: best...
    ✓ Downloaded: reel_ABC123.mp4 (3.5 MB)
```

---

## 📋 Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| Python | 3.7+ | Runtime |
| requests | 2.28+ | HTTP requests |
| beautifulsoup4 | 4.12+ | HTML parsing |
| yt-dlp | 2024+ | Video download |
| colorama | 0.4+ | Terminal colors |

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**aim914**

![GitHub](https://img.shields.io/badge/GitHub-aim914-181717?style=for-the-badge&logo=github&logoColor=white)

---

## ⭐ Star History

If this tool helped you, give it a ⭐ on GitHub!

---

```
╔══════════════════════════════════════════════════════════════╗
║  Made with ❤️ by aim914                                      ║
║  Instagram | TikTok | YouTube Video Downloader              ║
╚══════════════════════════════════════════════════════════════╝
```
