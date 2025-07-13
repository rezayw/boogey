from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading

NUM_BROWSERS = 5
NUM_VISITS = 3
VISIT_DURATION = 10  # seconds

def visit(domain):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    try:
        url = f"https://{domain}"
        for _ in range(NUM_VISITS):
            driver.get(url)
            time.sleep(VISIT_DURATION)
    except Exception as e:
        print(f"[!] Browser error: {e}")
    finally:
        driver.quit()

def run_browser_js_stress(domain):
    print(f"[+] Running BROWSER-JS-STRESS on {domain}")
    threads = []
    for _ in range(NUM_BROWSERS):
        t = threading.Thread(target=visit, args=(domain,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"[✓] BROWSER-JS-STRESS complete")