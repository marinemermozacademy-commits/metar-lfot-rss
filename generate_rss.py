import requests
import os
from datetime import datetime

API_KEY = os.environ["CHECKWX_API_KEY"]
ICAO = "LFOT"

headers = {"X-API-Key": API_KEY}

# METAR
metar_url = f"https://api.checkwx.com/metar/{ICAO}"
metar_data = requests.get(metar_url, headers=headers).json()
metar = metar_data["data"][0]

# TAF
taf_url = f"https://api.checkwx.com/taf/{ICAO}"
taf_data = requests.get(taf_url, headers=headers).json()
taf = taf_data["data"][0]

now = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

description = f"""LFOT<br><br>
🟢 METAR {metar.replace("METAR ", "")}<br><br>
🟡 TAF {taf.replace("TAF ", "")}
"""

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>METAR/TAF LFOT</title>
<description>Briefing météo aéronautique LFOT</description>
<lastBuildDate>{now}</lastBuildDate>

<item>
<title>LFOT - Météo aviation</title>
<description>{description}</description>
<pubDate>{now}</pubDate>
</item>

</channel>
</rss>
"""

with open("metar.xml", "w") as f:
    f.write(rss)
