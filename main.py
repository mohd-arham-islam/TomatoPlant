from fastapi import FastAPI, File, UploadFile, Response
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import requests


model = keras.models.load_model('tomato.h5')
class_names = ['Bacterial Spot',
            'Curl Virus',
            'Early Blight',
            'Healthy',
            'Late Blight',
            'Leaf Mold',
            'Mosaic Virus',
            'Septorial Leaf Spot',
            'Two Spotted Spider Mite']

app = FastAPI()

@app.get('/ping')
async def ping():
    return "Arham Islam"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))

    if image.shape[2] == 4:
        image = image[:, :, :3]

    return image.tolist()

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    prediction = model.predict(img_batch)[0]

    pos = np.argmax(prediction)
    return {
        'className': class_names[pos],
        'confidence': round(prediction[pos]*100, 1)
    }
    

