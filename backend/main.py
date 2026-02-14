import numpy as np 
import tensorflow as tf 
from fastapi import FastAPI,File,UploadFile
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
import io

#load model
model = tf.keras.models.load_model('./model/skin_cancer_model_final.h5')

#class labels
class_names = ["Benign" , "Malignant"]

app = FastAPI()

# allow frontend access

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
        allow_credentials=True
)


#image preprocessing function
def preprocess_image(image):
    image = image.resize((224,224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.post("/predict")

async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content).convert("RGB"))
    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2)
    }