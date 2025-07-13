# BOOGEY 
<p align="center" width="100%">
    <img width="50%%" src="https://blogger.googleusercontent.com/img/a/AVvXsEiivr3qEyKkFgqNmk8okRfuf6pMB1ZCCr3oEcjIgxr7JmJ0pLx-tvn4peGL_lqHEEK_Rx2GEzbpaLfaUf1bf8puTWLZTWevkM_cKz7MWgna3Hs1vUlCI2Nnwu8vfmzpF0z7rtMnW65fQwyx3zzNrmaEb7vb4jeTtapobsA5bYhP3wXlpQFI0Y0NQSBotLen"> 
</p>

### BOOGEY DEFENSE BOOTERS TESTING TOOLS

Boogey—better known as Albatross V2—isn’t just a name upgrade. The name might sound suspiciously close to "Booter," and hits like a freight train, and leaves the internet wondering if it just got punk’d.

## 📦 Features
<p align="center" width="100%">
    <img width="70%" src="https://blogger.googleusercontent.com/img/a/AVvXsEh4mYff_0wZPoCxcOJSH9pajS5x1ic0u5dRigNohjFFXa_5pb8ZxER6btmZAbajy3sR0AWsjINxYxNkzrY-_ieuLtlP9815-pPf0MCuCTkdI8ojY876K4ddHjiXMqc3lKZmely2j6WeAS0JTo1ucQkPuofDBuKlEzkpo68L3fbMyD_p0bFZHdOTZnV35HW3"> 
</p>

## ⚠️ Disclaimer
This tool is for **educational and authorized testing** only. Unauthorized use against external targets is strictly prohibited and illegal.

---

## 📁 Installation
```bash
git clone https://github.com/your-repo/cdn-penetration-tester.git
cd boogey
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🧪 Usage
```bash
python boogey.py
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