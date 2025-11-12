from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from AKS!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo/{name}")
def echo(name: str):
    return {"message": f"Hi {name}, welcome to AKS!"}
