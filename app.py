from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
def root():
    return {"message": "Hello from AKS!"}

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/echo/{name}")
def echo(name: str):
    return {"message": f"Hi {name}, welcome to AKS!"}
