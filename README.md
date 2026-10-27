# API de petits outils

![CI](https://github.com/Eliashrn/Projet-Versionning-Git/actions/workflows/ci.yml/badge.svg)
![Licence](https://img.shields.io/badge/licence-MIT-blue)

API web écrite en **Python avec FastAPI** qui expose de petites fonctions utilitaires (math, texte, conversion). Projet noté de versioning : le but est de travailler en équipe avec Git et GitHub (branches, issues, pull requests, revues croisées, CI/CD).

## Équipe

| Membre | Module |
|---|---|
| Eliashrn | math |
| _Nom du coéquipier_ | texte |
| _Nom du coéquipier_ | conversion |

Le module `validation` (facultatif à 3 membres) n'a pas été réalisé.

## Prérequis

- Python 3.12 ou plus récent
- Git
- (optionnel) Docker

## Installation

```bash
git clone https://github.com/Eliashrn/Projet-Versionning-Git.git
cd Projet-Versionning-Git

python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -r requirements-dev.txt
```

> Sous PowerShell, si l'activation est refusée : `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

L'API est disponible sur http://127.0.0.1:8000 et la documentation interactive (toutes les routes, avec leurs paramètres, testables dans le navigateur) sur http://127.0.0.1:8000/docs.

## Lancer avec Docker

```bash
docker build -t api-petits-outils .
docker run -p 8000:8000 api-petits-outils
```

Ou, depuis l'image publiée à chaque tag de version :

```bash
docker run -p 8000:8000 ghcr.io/eliashrn/projet-versionning-git:v1.0.0
```

## Routes

Toutes les routes sont en `GET`. Une entrée invalide renvoie une erreur **400** avec un message explicatif.

### État de l'API

| Route | Réponse |
|---|---|
| `/sante` | `{"status": "ok"}` |

### Module math

| Route | Exemple | Réponse |
|---|---|---|
| `/math/factorielle?n=5` | n entier entre 0 et 1000 | `{"resultat": 120}` |
| `/math/est_premier?n=7` | n entier positif ou nul | `{"resultat": true}` |
| `/math/pgcd?a=12&b=18` | a, b positifs, pas tous deux nuls | `{"resultat": 6}` |

### Module texte

Routes sous le préfixe `/texte` : `est_palindrome`, `compter_voyelles`, `inverser`.
Les paramètres exacts sont détaillés dans `/docs`.

### Module conversion

Routes sous le préfixe `/conversion` : `celsius_fahrenheit`, `km_miles`, `euros_devise`.
Les paramètres exacts sont détaillés dans `/docs`.

### Exemple d'erreur

```bash
curl "http://127.0.0.1:8000/math/factorielle?n=-1"
# 400 : {"detail": "n doit être positif ou nul"}
```

## Tests et qualité

```bash
pytest --cov=app        # tests + couverture (minimum exigé : 80 %)
ruff check .            # lint
```

Chaque fonction est couverte par au moins 3 tests : cas normal, cas limite, cas d'erreur.

## Structure du projet

```
.
├── app/
│   ├── main.py            # application FastAPI, route /sante, routeurs
│   ├── erreurs.py         # gestion d'erreurs partagée (erreur_400)
│   ├── math_outils.py     # module math
│   ├── texte.py           # module texte
│   └── conversion.py      # module conversion
├── tests/                 # tests pytest
├── .github/
│   ├── workflows/
│   │   ├── ci.yml         # ruff + pytest + couverture à chaque push et PR
│   │   └── deploy.yml     # publication de l'image Docker sur ghcr.io (tag v*)
│   └── pull_request_template.md
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```

## Workflow Git

- `main` est **protégée** : pull request obligatoire, 1 approbation, CI verte.
- Une **issue par fonctionnalité**, assignée à son auteur.
- Une **branche par issue**, par exemple `feat/8-module-math`.
- **Commits atomiques** au format [Conventional Commits](https://www.conventionalcommits.org/fr/) (`feat:`, `fix:`, `test:`, `docs:`, `ci:`, `chore:`).
- Chaque PR est **relue par un autre membre** avant le merge.
- Les conflits (notamment sur `app/erreurs.py`) sont résolus dans les PR.

## CI/CD

- **CI** (`ci.yml`) : lint `ruff`, tests `pytest` et couverture minimale de 80 % à chaque push et pull request.
- **Deploy** (`deploy.yml`) : à chaque tag `v*` (ex. `v1.0.0`), l'image Docker est construite et publiée sur `ghcr.io`.

## Licence

Distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE).
