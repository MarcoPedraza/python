#Creando api desde 0 con fastAPI


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hola Marco"

@app.get("/")
async def root():
    return "Hola Marco"


