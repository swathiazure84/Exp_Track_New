from fastapi import FastAPI
from routers.expences import expence_router
from fastapi.responses import RedirectResponse
app = FastAPI()


@app.get("/health")
def health():
    return "I am alive"

@app.get("/")
def root():
    return RedirectResponse(url='/docs')

app.include_router(expence_router)
