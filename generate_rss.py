import requests
import os

API_KEY = os.environ["CHECKWX_API_KEY"]
ICAO = "LFOT"

headers = {"X-API-Key": API_KEY}

# METAR (version stable)
metar_url = f"https://api.checkwx.com/v2/metar/{ICAO}/raw"
metar_data = requests.get(metar_url, headers=headers).json()

metar = "METAR indisponible"
if "data" in metar_data and len(metar_data["data"]) > 0:
    metar = metar_data["data"][0]

# TAF (version stable)
taf_url = f"https://api.checkwx.com/v2/taf/{ICAO}/raw"
taf_data = requests.get(taf_url, headers=headers).json()

taf = "TAF indisponible"
if "data" in taf_data and len(taf_data["data"]) > 0:
    taf = taf_data["data"][0]

# FORMAT AFFICHAGE SIGNAO
description = f"""🟢 {metar}

🟡 {taf}
"""

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>METAR LFOT</title>

<item>
<title>LFOT METAR/TAF</title>
<description>{description}</description>
</item>

</channel>
</rss>
"""
rss = rss.strip()

with open("metar.xml", "w", encoding="utf-8", newline="\n") as f:
    f.write(rss)
