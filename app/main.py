from fastapi import FastAPI

app = FastAPI(title="API de petits outils")


@app.get("/sante")
def sante():
    return {"status": "ok"}


# Routeurs des modules (un par membre)
# app.include_router(math_outils.router)
# app.include_router(texte.router)
# app.include_router(conversion.router)
# app.include_router(validation.router)