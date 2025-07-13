# BOOGEY 
<p align="center">

</p>

### BOOGEY DEFENSE BOOTERS TESTING TOOLS

Boogey—better known as Albatross V2—isn’t just a name upgrade. The name might sound suspiciously close to "Booter," and hits like a freight train, and leaves the internet wondering if it just got punk’d.

## 📦 Features
- HTTPS-STORM
- BROWSER-JS-STRESS (Headless Chrome)
- TLS-COOKIE-HOLD
- SPOOFED-HTTP2-RST
- CACHE-BYPASS-STORM
- ORIGIN-DOWN-PUSH
- Unified CLI with interactive menu and test timer

## ⚠️ Disclaimer
This tool is for **educational and authorized testing** only. Unauthorized use against external targets is strictly prohibited and illegal.

---

## 📁 Installation
```bash
git clone https://github.com/your-repo/cdn-penetration-tester.git
cd cdn-penetration-tester
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🧪 Usage
```bash
python cdn_penetration_tester.py
```
Follow the on-screen prompts:
1. Enter the domain (e.g. `example.com`)
2. Select the test mode
3. Choose a run time (3 minutes, 30 minutes, 1 hour)
4. Review auto-generated report in `reports/` directory

---

## 🧱 Modules Overview
| Module                  | Description                                                   |
|------------------------|---------------------------------------------------------------|
| `https_storm.py`       | Sends high-RPS HTTPS GET requests using `httpx`               |
| `browser_js_stress.py` | Launches headless browsers with Selenium for JS challenge     |
| `tls_cookie_hold.py`   | Holds TLS connections open to exhaust server socket pools     |
| `http2_rst.py`         | Simulates HTTP/2 RST_STREAM flood (CVE-2023-44487)            |
| `cache_bypass_storm.py`| Sends uncached requests to origin using headers + UUID params |
| `origin_down_push.py`  | Probes for real origin IPs and sends direct HTTP requests     |

## 📜 License
MIT (Modify for legal compliance and usage limitations)

---

For more help or module customization, contact your security team or red team operations leader.
