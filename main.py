# libreria fastapi
from fastapi import FastAPI
# permite el uso de HTML 
from fastapi.responses import HTMLResponse

# constructor asignar valores a los elementos de clase cuando se crea un objeto de esa misma clase
app = FastAPI()

# enpoint metodo GET
@app.get("/")
# Esta función será llamada por FastAPI cada vez que reciba un request en la URL "/"
async def root():
# llamamos a la libreria HTMLResponse par poder usar etiquetas html
    return HTMLResponse('<h1>Hello World</h1>')

