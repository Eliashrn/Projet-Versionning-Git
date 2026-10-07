from fastapi import HTTPException


def erreur_400(message: str):
    """Lève une erreur 400 avec un message clair."""
    raise HTTPException(status_code=400, detail=message)