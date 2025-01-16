from fastapi import FastAPI

app = FastAPI()

@app.get("/namaste")
def namaste():
    return {"greeting": "Namaste"}
