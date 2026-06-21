# Web Scraper + Video Download Tool

Python tool for web scraping and video downloading from multiple platforms.

## Features

### Search
- Web search via DuckDuckGo
- Search keywords on any website
- Search links on any website

### Scrape
- Text extraction (CSS selectors)
- Links extraction
- Images extraction
- Table data extraction

### Download
- Video download with quality selection (Best/720p/480p/360p)
- File download with auto-detection
- Batch image download

## Supported Platforms

| Platform | Video Download |
|----------|----------------|
| Instagram Reels | ✅ |
| TikTok | ✅ |
| YouTube Shorts | ✅ |
| YouTube Videos | ✅ |
| Twitter/X Videos | ✅ |
| Facebook Videos | ✅ |
| Reddit Videos | ✅ |
| Any Website | ✅ |

## Supported File Formats (Auto-Detect)

Images: JPG, PNG, GIF, WebP, SVG, BMP
Videos: MP4, WebM, MKV, AVI, MOV
Audio: MP3, WAV, OGG, FLAC, M4A
Documents: PDF, DOC, DOCX, XLS, XLSX
Archives: ZIP, RAR, 7Z, TAR, GZ
Other: APK, EXE, TXT, CSV, JSON, XML, HTML

## Installation

### 1. Install Python packages
```bash
pip install -r requirements.txt
```

### 2. Install yt-dlp
```bash
pip install yt-dlp
```

### 3. (Optional) Install ffmpeg for video processing
```bash
# Termux
pkg install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

## Usage

```bash
python web_scraper.py
```

### Menu Options
1. Web search - Search anything on DuckDuckGo
2. Website pe keyword - Find specific content on a website
3. Website pe links - Find links on a website
4. Text scrape - Extract text using CSS selectors
5. Links scrape - Extract all links from a page
6. Images scrape - Extract all images from a page
7. Video download - Download videos with quality selection
8. File download - Download any file with auto-detection
9. Images download - Download all images from a page

## Examples

### Download Instagram Reel
```
Select (7): Video download
Paste link: https://www.instagram.com/reel/ABC123/
Quality: 1 (Best)
```

### Download YouTube Short
```
Select (7): Video download
Paste link: https://youtube.com/shorts/ABC123
Quality: 2 (720p)
```

### Scrape Website Text
```
Select (4): Text scrape
URL: https://example.com
CSS selector: h1, p, .class-name
```

## Save Location

All downloads are saved to:
```
/storage/emulated/0/only for work/downloads/
```

## Requirements

- Python 3.7+
- Internet connection
- yt-dlp (for video downloads)
- ffmpeg (optional, for video processing)

## License

MIT License

## Author

aim914
