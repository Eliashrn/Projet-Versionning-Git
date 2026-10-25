from math import gcd

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


def pgcd(a: int, b: int) -> int:
    """Plus grand commun diviseur de a et b (positifs, pas tous les deux nuls)."""
    if a < 0 or b < 0:
        raise ValueError("a et b doivent être positifs ou nuls")
    if a == 0 and b == 0:
        raise ValueError("a et b ne peuvent pas être tous les deux nuls")
    return gcd(a, b)


@router.get("/pgcd")
def route_pgcd(a: int, b: int):
    try:
        return {"resultat": pgcd(a, b)}
    except ValueError as e:
        erreur_400(str(e))