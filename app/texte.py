from fastapi import APIRouter

from app.erreurs import erreur_400

router = APIRouter(prefix="/texte", tags=["texte"])


def est_palindrome(mot: str) -> bool:
    nettoye = "".join(c.lower() for c in mot if c.isalnum())
    if not nettoye:
        erreur_400("Le mot ne peut pas être vide")
    return nettoye == nettoye[::-1]


@router.get("/est_palindrome/{mot}")
def route_est_palindrome(mot: str):
    return {"mot": mot, "resultat": est_palindrome(mot)}