from fastapi import FastAPI
from routers.expences import expence_router
app = FastAPI()


@app.get("/health")
def health():
    return "I am alive"

@app.get("/")
def root():
    return "welcome to expensce tracker"

app.include_router(expence_router)
