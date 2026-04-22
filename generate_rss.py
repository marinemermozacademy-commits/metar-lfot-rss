import requests
import os
import html
from datetime import datetime

API_KEY = os.environ["CHECKWX_API_KEY"]
ICAO = "LFOT"

headers = {"X-API-Key": API_KEY}

metar_url = f"https://api.checkwx.com/v2/metar/{ICAO}/raw"
taf_url = f"https://api.checkwx.com/v2/taf/{ICAO}/raw"

metar_data = requests.get(metar_url, headers=headers).json()
taf_data = requests.get(taf_url, headers=headers).json()

metar_list = metar_data.get("data", [])
taf_list = taf_data.get("data", [])

metar = metar_list[0] if metar_list else "METAR indisponible"
taf = taf_list[0] if taf_list else "TAF indisponible"

metar = html.escape(metar)
taf = html.escape(taf)

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

description = f"""🟢 {metar}

🟡 {taf}"""

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>METAR LFOT</title>
<lastBuildDate>{now}</lastBuildDate>

<item>
<title>LFOT METAR/TAF</title>
<description>{description}</description>
<pubDate>{now}</pubDate>
</item>

</channel>
</rss>
"""

with open("metar.xml", "w", encoding="utf-8", newline="\n") as f:
    f.write(rss)
