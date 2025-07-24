from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI! ECS service is auomatically deployed."}

@app.get("/health")
def health_check():
    return {"status": "ok"}
