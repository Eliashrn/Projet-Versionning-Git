from fastapi import APIRouter

from app.erreurs import erreur_400

router = APIRouter(prefix="/math", tags=["math"])

LIMITE_FACTORIELLE = 1000


def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    if n > LIMITE_FACTORIELLE:
        raise ValueError(f"n doit être inférieur ou égal à {LIMITE_FACTORIELLE}")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


@router.get("/factorielle")
def route_factorielle(n: int):
    try:
        return {"resultat": factorielle(n)}
    except ValueError as e:
        erreur_400(str(e))



def est_premier(n: int) -> bool:
    """Indique si n est un nombre premier (n >= 0)."""
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@router.get("/est_premier")
def route_est_premier(n: int):
    try:
        return {"resultat": est_premier(n)}
    except ValueError as e:
        erreur_400(str(e))