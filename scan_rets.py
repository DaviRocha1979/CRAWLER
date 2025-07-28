import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib.parse

KEYWORDS = [
    "cooperação", "formação", "saúde pública", "OPAS", "OMS",
    "tuberculose", "malária", "vacinação", "CPLP", "doenças tropicais"
]

def full_url(base, link):
    return urllib.parse.urljoin(base, link)

def scan_site(base_url):
    try:
        resp = requests.get(base_url, timeout=10)
        resp.raise_for_status()
    except Exception:
        return []
    soup = BeautifulSoup(resp.text, "html.parser")
    matches = []
    for a in soup.find_all("a", href=True):
        text = a.get_text().strip()
        href = a["href"]
        if any(kw.lower() in text.lower() for kw in KEYWORDS):
            matches.append({"title": text, "url": full_url(base_url, href)})
    return matches

def main():
    with open("RETS_reorganizado.csv", newline="") as f:
        reader = csv.DictReader(f)
        out = []
        for row in reader:
            for match in scan_site(row["URL"]):
                out.append({
                    "categoria": row["Categoria"],
                    "pais": row["País"],
                    "base_url": row["URL"],
                    "titulo": match["title"],
                    "link": match["url"]
                })
            time.sleep(1)
    if out:
        with open("matches_rets.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=out[0].keys())
            writer.writeheader()
            writer.writerows(out)

if __name__ == "__main__":
    main()
