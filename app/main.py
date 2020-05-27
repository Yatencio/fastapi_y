from fastapi import FastAPI

app = FastAPI()


@app.get("/hola")
def read_hola():
    return {"hola": "hola yoharis"}
    
@app.get("/mundo")
def read_mundo():
    return {"hola": "hola migue"}