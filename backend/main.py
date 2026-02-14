import numpy as np 
import tensorflow as tf 
from fastapi import FastAPI,File,UploadFile
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

#load model
model = tf.keras.models.load_model('./model/skin_cancer_model_final.h5')

#class labels
class_names = ["Benign" , "Malignant"]

app = FastAPI()
