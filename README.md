# 🚀 Installation de Python, Django et configuration de l’environnement virtuel (venv)

## 🐍 1. Installation de Python
Vérifie si Python est déjà installé :
```powershell
python --version
```
ou
```powershell
py --version
```

Si ce n’est pas le cas, installe-le via le Microsoft Store :
```powershell
winget install Python.Python.3.12
```

---

## ⚙️ 2. Mise à jour de pip
```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

---

## 🧰 3. Création de l’environnement virtuel
Dans le dossier du projet :
```powershell
events/event_list.html
```

Active l’environnement virtuel :
```powershell
.\.venv\Scripts\Activate
```

---

## ⚠️ Problème : "l’exécution de scripts est désactivée"
Si tu obtiens cette erreur :
```
Impossible de charger le fichier Activate.ps1 car l’exécution de scripts est désactivée sur ce système.
```

➡️ Solution temporaire :
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

➡️ Solution permanente (recommandée) :
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Puis réactive ton environnement :
```powershell
.\.venv\Scripts\Activate
```

---

## 🌐 4. Installation de Django
Une fois le venv activé :
```powershell
pip install django
```

Vérifie l’installation :
```powershell
django-admin --version
```

---

## ⚡ 5. Créer et lancer un projet Django
```powershell
django-admin startproject mon_projet
cd mon_projet
python manage.py runserver
```

Le serveur est accessible sur :
👉 http://127.0.0.1:8000/

---

## 🧩 Résumé rapide
| Étape | Commande principale |
|-------|---------------------|
| Installer Python | `winget install Python.Python.3.12` |
| Créer venv | `python -m venv .venv` |
| Activer venv | `.\.venv\Scripts\Activate` |
| Corriger exécution scripts | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` |
| Installer Django | `pip install django` |
| Lancer projet | `python manage.py runserver` |

---

💡 **Conseil :** garde ton environnement virtuel activé pendant tout ton travail sur le projet pour éviter les conflits de versions.
