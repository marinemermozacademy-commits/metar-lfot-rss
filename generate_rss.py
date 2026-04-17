import requests
import os
from datetime import datetime

API_KEY = os.environ["CHECKWX_API_KEY"]
ICAO = "LFOT"

url = f"https://api.checkwx.com/metar/{ICAO}"
headers = {"X-API-Key": API_KEY}

r = requests.get(url, headers=headers)
data = r.json()

metar = data["data"][0]
now = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>METAR LFOT</title>
<description>METAR Tours Val de Loire</description>
<link>https://github.com/{ICAO}</link>
<lastBuildDate>{now}</lastBuildDate>
<item>
<title>LFOT METAR</title>
<description>{metar}</description>
<pubDate>{now}</pubDate>
</item>
</channel>
</rss>
"""

with open("metar.xml", "w") as f:
    f.write(rss)
