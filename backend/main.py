import numpy as np 
import tensorflow as tf 
from fastapi import FastAPI,File,UploadFile
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
