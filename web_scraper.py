import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import os
import re
import subprocess
from urllib.parse import urlparse, unquote

class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.download_dir = "/storage/emulated/0/only for work/downloads"
        os.makedirs(self.download_dir, exist_ok=True)

    def auto_detect(self, url, data, headers):
        ext = self._detect_from_content_type(headers)
        if ext: return ext
        ext = self._detect_from_url(url)
        if ext: return ext
        ext = self._detect_from_magic(data)
        if ext: return ext
        return 'bin'

    def _detect_from_content_type(self, headers):
        ct = headers.get('Content-Type', '').lower().split(';')[0].strip()
        mime_map = {
            'image/jpeg': 'jpg', 'image/png': 'png', 'image/gif': 'gif',
            'image/webp': 'webp', 'video/mp4': 'mp4', 'video/webm': 'webm',
            'audio/mpeg': 'mp3', 'application/pdf': 'pdf', 'application/zip': 'zip',
            'text/html': 'html', 'text/plain': 'txt',
        }
        return mime_map.get(ct)

    def _detect_from_url(self, url):
        try:
            ext = unquote(urlparse(url).path).split('.')[-1].split('?')[0].lower()
            if ext in ['jpg','png','gif','webp','mp4','webm','mkv','avi','mov','mp3','wav','pdf','zip','txt']:
                return ext
        except: pass
        return None

    def _detect_from_magic(self, data):
        if not data or len(data) < 4: return None
        h = data[:16]
        if h[:8] == b'\x89PNG\r\n\x1a\n': return 'png'
        if h[:3] == b'\xff\xd8\xff': return 'jpg'
        if h[:4] == b'%PDF': return 'pdf'
        if h[:2] == b'PK': return 'zip'
        if h[:4] == b'ftyp': return 'mp4'
        return None

    def download_video(self, url, quality="best"):
        print(f"\n{'='*55}")
        print(f"VIDEO: {url}")
        print(f"Quality: {quality}")
        print(f"{'='*55}")

        output_template = os.path.join(self.download_dir, "%(title).70s.%(ext)s")

        formats_to_try = [
            "best",
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "bestvideo+bestaudio/best",
            "worst",
        ]

        if quality == "720":
            formats_to_try = [
                "bestvideo[height<=720]+bestaudio/best[height<=720]",
                "best[height<=720]",
                "best",
            ]
        elif quality == "480":
            formats_to_try = [
                "bestvideo[height<=480]+bestaudio/best[height<=480]",
                "best[height<=480]",
                "best",
            ]
        elif quality == "360":
            formats_to_try = [
                "bestvideo[height<=360]+bestaudio/best[height<=360]",
                "best[height<=360]",
                "best",
            ]

        for fmt in formats_to_try:
            cmd = [
                "yt-dlp",
                "-f", fmt,
                "--no-check-certificates",
                "--no-warnings",
                "-o", output_template,
                "--no-overwrites",
                "--print", "after_move:filepath",
                url
            ]

            try:
                print(f"Trying: {fmt[:50]}...")
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)

                if result.returncode == 0:
                    filepath = result.stdout.strip().split('\n')[-1]
                    if filepath and os.path.exists(filepath):
                        size = os.path.getsize(filepath)
                        sz = f"{size/(1024*1024):.1f} MB" if size > 1024*1024 else f"{size/1024:.1f} KB"
                        print(f"Downloaded: {filepath} ({sz})")
                        return filepath
                    else:
                        files = sorted(os.listdir(self.download_dir),
                                       key=lambda x: os.path.getmtime(os.path.join(self.download_dir, x)), reverse=True)
                        if files:
                            latest = os.path.join(self.download_dir, files[0])
                            if os.path.getmtime(latest) > time.time() - 60:
                                size = os.path.getsize(latest)
                                print(f"Found: {latest} ({size/(1024*1024):.1f} MB)")
                                return latest
                else:
                    err = result.stderr[:200] if result.stderr else ""
                    if "format" in err.lower():
                        print(f"  Format not available, trying next...")
                        continue
                    else:
                        print(f"  Error: {err[:100]}")
                        continue

            except subprocess.TimeoutExpired:
                print("  Timeout, trying next...")
                continue
            except FileNotFoundError:
                subprocess.run(["pip", "install", "yt-dlp"], capture_output=True)
                return self.download_video(url, quality)
            except Exception as e:
                print(f"  Error: {e}")
                continue

        return self._direct_video_download(url)

    def _direct_video_download(self, url):
        try:
            html = self.fetch_text(url)
            if not html: return None

            patterns = [
                r'(https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*)',
                r'"(https?://[^"]*\.mp4[^"]*)"',
                r"'(https?://[^']*\.mp4[^']*)'",
            ]
            for pattern in patterns:
                matches = re.findall(pattern, html)
                if matches:
                    best = matches[0]
                    for m in matches:
                        if any(x in m for x in ['googlevideo','fbcdn','cdninstagram','twimg','v.redd.it']):
                            best = m
                            break
                    print(f"Direct link mila!")
                    return self.download_file(best)
        except: pass
        return None

    def download_file(self, url, filename=None):
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        print(f"\nDownloading: {url[:80]}...")
        try:
            resp = self.session.get(url, stream=True, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"Failed: {e}")
            return None

        content_type = resp.headers.get('Content-Type', '')
        chunks = []
        for chunk in resp.iter_content(chunk_size=65536):
            if chunk: chunks.append(chunk)
        data = b''.join(chunks)
        if not data: print("Empty!"); return None

        ext = self.auto_detect(url, data, resp.headers)
        if not filename:
            cd = resp.headers.get('Content-Disposition', '')
            filename = self._make_filename(url, cd, ext)

        filepath = os.path.join(self.download_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(data)

        size = len(data)
        if size > 1024*1024: sz = f"{size/(1024*1024):.1f} MB"
        elif size > 1024: sz = f"{size/1024:.1f} KB"
        else: sz = f"{size} B"
        print(f"Saved: {filepath} ({sz})")
        return filepath

    def _make_filename(self, url, content_disp, ext):
        if content_disp:
            match = re.search(r'filename[*]?=["\']?([^"\';\s]+)', content_disp)
            if match:
                name = re.sub(r'[<>:"/\\|?*]', '_', unquote(match.group(1)))
                if '.' not in name: name = f"{name}.{ext}"
                return name
        path = urlparse(url).path
        name = os.path.basename(unquote(path)).split('?')[0]
        if name and '.' in name:
            name = f"{name.rsplit('.',1)[0]}.{ext}"
        else:
            name = f"file_{int(time.time())}.{ext}"
        return re.sub(r'[<>:"/\\|?*]', '_', name)

    def fetch_text(self, url, delay=0):
        try:
            time.sleep(delay)
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def parse(self, html):
        return BeautifulSoup(html, 'html.parser')

    def web_search(self, query, num=10):
        url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
        try:
            resp = self.session.get(url, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            results = []
            for r in soup.select('div.result'):
                title_el = r.select_one('a.result__a')
                desc_el = r.select_one('a.result__snippet')
                if title_el:
                    results.append({
                        'title': title_el.get_text(strip=True),
                        'url': title_el.get('href', ''),
                        'description': desc_el.get_text(strip=True) if desc_el else ''
                    })
            return results[:num]
        except: return []

    def extract_text(self, soup, sel):
        return [el.get_text(strip=True) for el in soup.select(sel)]

    def extract_links(self, soup, sel):
        return [{'text': el.get_text(strip=True), 'url': el.get('href', '')} for el in soup.select(sel)]

    def extract_images(self, soup, sel):
        return [{'src': img.get('src', ''), 'alt': img.get('alt', '')} for img in soup.select(sel)]

    def search_links(self, url, keyword):
        html = self.fetch_text(url)
        if not html: return []
        soup = self.parse(html)
        results = []
        kw = keyword.lower()
        base_url = url.rstrip('/')
        for a in soup.find_all('a', href=True):
            text = a.get_text(strip=True)
            href = a['href']
            full = href if href.startswith(('http://', 'https://')) else base_url + '/' + href.lstrip('/')
            if kw in text.lower() or kw in href.lower():
                results.append({'text': text, 'url': full})
        return results

    def download_all_images(self, url, selector='img'):
        html = self.fetch_text(url)
        if not html: return []
        soup = self.parse(html)
        images = self.extract_images(soup, selector)
        downloaded = []
        for img in images:
            src = img['src']
            if not src.startswith(('http://', 'https://')):
                src = url.rstrip('/') + '/' + src.lstrip('/')
            result = self.download_file(src)
            if result: downloaded.append(result)
        print(f"\n{len(downloaded)} images downloaded!")
        return downloaded


def main():
    s = WebScraper()

    print("=" * 55)
    print("   WEB SCRAPER + VIDEO DOWNLOAD TOOL")
    print("   Instagram | TikTok | YouTube | Twitter | Facebook")
    print("=" * 55)

    while True:
        print("\n--- SEARCH ---")
        print("1. Web search")
        print("2. Website pe keyword")
        print("3. Website pe links")
        print("\n--- SCRAPE ---")
        print("4. Text scrape")
        print("5. Links scrape")
        print("6. Images scrape")
        print("\n--- DOWNLOAD ---")
        print("7. Video download (quality choose karo)")
        print("8. File download (auto-detect)")
        print("9. Saari images download")
        print("\n--- OTHER ---")
        print("10. Exit")

        choice = input("\nSelect (1-10): ").strip()

        if choice == '10':
            print("Bye!")
            break

        if choice == '1':
            query = input("\nSearch: ").strip()
            if not query: continue
            results = s.web_search(query)
            if not results:
                print("Kuch nahi mila!"); continue
            for i, r in enumerate(results, 1):
                print(f"\n{i}. {r['title']}")
                print(f"   {r['url']}")
                if r['description']: print(f"   {r['description'][:150]}")
            dl = input("\nVideo download? (number/no): ").strip()
            if dl.isdigit() and 1 <= int(dl) <= len(results):
                s.download_video(results[int(dl)-1].get('url',''))

        elif choice == '2':
            url = input("URL: ").strip()
            if not url.startswith(('http://', 'https://')): url = 'https://' + url
            kw = input("Keyword: ").strip()
            if not kw: continue
            results = s.search_links(url, kw)
            if not results:
                print("Kuch nahi mila!"); continue
            print(f"\n{len(results)} links:")
            for i, r in enumerate(results, 1):
                print(f"{i}. {r['text'][:60]} -> {r['url'][:100]}")
            dl = input("\nDownload? (number/no): ").strip()
            if dl.isdigit() and 1 <= int(dl) <= len(results):
                s.download_video(results[int(dl)-1]['url'])

        elif choice == '3':
            url = input("URL: ").strip()
            if not url.startswith(('http://', 'https://')): url = 'https://' + url
            kw = input("Keyword: ").strip()
            if not kw: continue
            for i, r in enumerate(s.search_links(url, kw), 1):
                print(f"{i}. {r['text'][:60]} -> {r['url'][:100]}")

        elif choice in ['4','5','6']:
            url = input("URL: ").strip()
            if not url.startswith(('http://', 'https://')): url = 'https://' + url
            html = s.fetch_text(url)
            if not html: print("Failed!"); continue
            soup = s.parse(html)
            print("Page loaded!")
            if choice == '4':
                sel = input("CSS selector: ").strip()
                for i, t in enumerate(s.extract_text(soup, sel)[:15], 1): print(f"{i}. {t[:120]}")
            elif choice == '5':
                sel = input("CSS selector: ").strip()
                for i, l in enumerate(s.extract_links(soup, sel)[:15], 1): print(f"{i}. {l['text'][:60]} -> {l['url'][:100]}")
            elif choice == '6':
                sel = input("Selector (default: img): ").strip() or 'img'
                data = s.extract_images(soup, sel)
                for i, img in enumerate(data[:15], 1): print(f"{i}. {img['alt'][:40]} -> {img['src'][:100]}")
                if input("\nDownload all? (y/n): ").strip().lower() == 'y':
                    s.download_all_images(url, sel)

        elif choice == '7':
            print("\n--- VIDEO DOWNLOAD ---")
            print("Instagram | TikTok | YouTube Shorts/Long")
            print("Twitter/X | Facebook | Reddit | Any site")
            print("-" * 45)
            url = input("\nPaste video link: ").strip()
            if not url: continue

            print("\nQuality choose karo:")
            print("1. Best (original quality)")
            print("2. 720p (HD)")
            print("3. 480p (SD)")
            print("4. 360p (Low)")
            q = input("Select (1-4, default=1): ").strip()

            quality_map = {'1': 'best', '2': '720', '3': '480', '4': '360'}
            quality = quality_map.get(q, 'best')
            s.download_video(url, quality)

        elif choice == '8':
            url = input("URL: ").strip()
            s.download_file(url)

        elif choice == '9':
            url = input("URL: ").strip()
            if not url.startswith(('http://', 'https://')): url = 'https://' + url
            s.download_all_images(url)

if __name__ == "__main__":
    main()
