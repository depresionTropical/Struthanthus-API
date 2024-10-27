# main.py
from typing import  Literal
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse

from pydantic import BaseModel
from module.res_net import predict_class
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Struthanthus API",
    description="API para predecir la clase de una imagen usando ResNet.",
    version="0.1.0",
    contact={
        "name": "AAAIMX",
        "url": "https://github.com/aaaimx",
        "email": "contact@aaaimx.org",
    },
    docs_url="/doc", redoc_url=None
)
# Permitir acceso desde cualquier origen temporalmente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionResponse(BaseModel):
    class_predicted: Literal[0, 1]

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/doc")

@app.post(
    "/upload-image/",
    summary="Subir imagen",
    description="Sube una imagen y predice su clase usando ResNet.",
    tags=["Image Classification"],
    response_description="La clase predicha de la imagen.\n 0: No es Muérdago\n 1: Es Muérdago",
    response_model=PredictionResponse
)
async def upload_image(file: UploadFile = File(...)):
    """
    Asynchronously uploads an image and predicts its class.

    Args:
        file (UploadFile): The image file to be uploaded.

    Returns:
        dict: A dictionary with the key 'class_predicted' and an integer value which can only be 0 or 1.

    Raises:
        ValueError: If the predicted class is not 0 or 1.
    """
    class_predicted = predict_class.predict_image_class(file.file)

    return {"class_predicted": int(class_predicted)}
