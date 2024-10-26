# main.py
from fastapi import FastAPI, File, UploadFile

from module.res_net import predict_class

app = FastAPI()


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    class_predicted = predict_class.predict_image_class(file.file)
    return { "class_predicted": class_predicted}
