# model_handler.py
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image

class ModelHandler:
    def __init__(self):
        self.model = MobileNetV2(weights='imagenet')  # Load the MobileNetV2 pre-trained model
    
    def preprocess_image(self, img):
        img = img.resize((224, 224))  # Resize image to 224x224 for MobileNetV2
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return preprocess_input(img_array)

    def predict(self, img):
        processed_img = self.preprocess_image(img)
        predictions = self.model.predict(processed_img)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        return decoded_predictions