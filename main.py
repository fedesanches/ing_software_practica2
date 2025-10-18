from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class FileRequest(BaseModel):
    name: str
    content: str

@app.get("/files")
async def prueba_root():
    """ Devuelve una lista de los archivos disponibles en el directorio files. """

    files = os.listdir("files")
    return {"files": files}

@app.post("/files")
async def crear_archivo(request: FileRequest):
    """ Crea un archivo con el nombre y contenido especificados en el directorio files. """

    with open(f"files/{request.name}", "w") as f:
        f.write(request.content)
    
    return {"mensaje": f"Archivo '{request.name}' creado exitosamente."}

@app.get("/files/{file_name}")
async def leer_archivo(file_name: str):
    """ Lee el contenido de un archivo específico en el directorio files. """

    file_path = os.path.join("files", file_name)
    if not os.path.isfile(file_path):
        return {"error": "Archivo no encontrado."}

    with open(file_path, "r") as f:
        content = f.read()
    
    return {"name": file_name, "content": content}