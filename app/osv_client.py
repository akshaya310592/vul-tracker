import httpx
from cachetools import TTLCache, cached

# Cache for 10 minutes, up to 1000 entries
cache = TTLCache(maxsize=1000, ttl=600)

@cached(cache)
def get_vulnerabilities(package: str, version: str) -> list:
    url = "https://api.osv.dev/v1/query"
    payload = {
        "version": version,
        "package": {
            "name": package,
            "ecosystem": "PyPI"
        }
    }

    try:
        response = httpx.post(url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("vulns", [])
    except Exception as e:
        print(f"Error fetching {package}: {e}")
        return []
