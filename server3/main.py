from fastapi import FastAPI

app = FastAPI()

@app.get("/halo")
def halo():
    return {"greeting": "Halo"}
