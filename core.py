import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

from flask import Flask, render_template, request
import json
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
model = load_model("nn_model.h5") 

@app.route('/', methods = ["GET", "POST"])
def index():
    data = request.get_json()
    if data != None:
        img = preprocess_img(data["ImageData"])
        result = recognize(img) 
        return json.dumps({'answer' : str(result)})
    else:
        return render_template('index.html')


def recognize(img):
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
    
    im = Image.open(BytesIO(imgdata))
   
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im,im)
    
    img = img_to_array(bg)
    img /= 255
    result = []
    
    for i in img:
        for j in i:
            if j[0] == 1:
                result.append(0)
            else:
                result.append(1)
    return np.array([result])
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
