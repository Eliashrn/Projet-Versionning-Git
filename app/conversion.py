from fastapi import APIRouter

from app.erreurs import erreur_400

router = APIRouter(prefix="/conversion", tags=["conversion"])

TAUX_EUROS = {"USD": 1.08, "GBP": 0.86, "JPY": 160.0}
ZERO_ABSOLU = -273.15
MILES_PAR_KM = 0.621371


def celsius_fahrenheit(c: float) -> float:
    if c < ZERO_ABSOLU:
        raise ValueError("la température ne peut pas être sous -273.15 °C")
    return c * 9 / 5 + 32


def km_miles(km: float) -> float:
    if km < 0:
        raise ValueError("la distance ne peut pas être négative")
    return km * MILES_PAR_KM


def euros_devise(montant: float, devise: str) -> float:
    if montant < 0:
        raise ValueError("le montant ne peut pas être négatif")
    code = devise.upper()
    if code not in TAUX_EUROS:
        raise ValueError(f"devise inconnue : {devise}")
    return montant * TAUX_EUROS[code]


@router.get("/celsius-fahrenheit/{c}")
def route_celsius_fahrenheit(c: float):
    try:
        return {"celsius": c, "fahrenheit": celsius_fahrenheit(c)}
    except ValueError as e:
        erreur_400(str(e))


@router.get("/km-miles/{km}")
def route_km_miles(km: float):
    try:
        return {"kilometres": km, "miles": km_miles(km)}
    except ValueError as e:
        erreur_400(str(e))


@router.get("/euros-devise/{montant}/{devise}")
def route_euros_devise(montant: float, devise: str):
    try:
        return {
            "montant": montant,
            "devise": devise.upper(),
            "resultat": euros_devise(montant, devise),
        }
    except ValueError as e:
        erreur_400(str(e))