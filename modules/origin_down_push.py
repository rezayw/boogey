import socket
import requests
import dns.resolver
import time

COMMON_SUBS = ["mail", "ftp", "cpanel", "webmail", "direct", "dev"]


def discover_origin_ip(domain):
    print(f"[+] Attempting origin IP discovery for {domain}...")
    ip_candidates = set()
    for sub in COMMON_SUBS:
        try:
            fqdn = f"{sub}.{domain}"
            ip = socket.gethostbyname(fqdn)
            ip_candidates.add((fqdn, ip))
        except socket.gaierror:
            continue
    return ip_candidates


def test_origin(ip, domain):
    headers = {"Host": domain}
    try:
        response = requests.get(f"http://{ip}", headers=headers, timeout=5)
        print(f"[✓] Origin {ip} responded with {response.status_code}")
    except Exception as e:
        print(f"[!] Failed to reach origin {ip}: {e}")


def run_origin_down_push(domain):
    print(f"[+] Running ORIGIN-DOWN-PUSH on {domain}")
    origins = discover_origin_ip(domain)
    if not origins:
        print("[-] No likely origin IPs found.")
        return

    for sub, ip in origins:
        print(f"[→] Testing subdomain {sub} with IP {ip}...")
        test_origin(ip, domain)
    print("[✓] ORIGIN-DOWN-PUSH complete.")