import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

from flask import Flask, render_template, request
import json
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    data = request.get_json()
    if data != None:
        img = preprocess_img(data["ImageData"])
        result = recognize(img) 
        print(result)
        return json.dumps({'answer' : str(result)})
    else:
        return render_template('index.html')


def recognize(img):
    model = load_model("C:\kedr\\nn_model.h5") 
    result = model.predict(img)[0]
    return max_index(result)
       

def max_index(arr):
    max_val = -1
    max_i = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_i = i
    return max_i
        
        
def preprocess_img(image):
    imgdata = base64.b64decode(image)
    loaded_image = Image.open(BytesIO(imgdata))
    loaded_image.save("C:\\kedr\\test.png")
    
    im = Image.open("C:\\kedr\\test.png")
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im,im)
    bg.save("C:\\kedr\\test.png")
    
    img = load_img("C:\\kedr\\test.png")
    img = img_to_array(img)
    img /= 255
    result = []
    
    for i in img[0]:
        for j in i:
            if j == 1:
                result.append(0)
            else:
                result.append(1)
    return np.array([result])
    

if __name__ == "__main__":
    pass
