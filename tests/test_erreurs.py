import pytest
from fastapi import HTTPException

from app.erreurs import erreur_400


def test_erreur_400_leve_une_exception():
    with pytest.raises(HTTPException) as info:
        erreur_400("entrée invalide")
    assert info.value.status_code == 400
    assert info.value.detail == "entrée invalide"