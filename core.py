import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def recognize(img):
    model = load_model("nn_model.h5") 
    result = model.predict(img)
    return result
       

def max_index(arr):
    max_val = -1
    max_i = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_i = i
    return max_i
        
        
def preprocess_img(image):
    img = load_img(image)
    img = img_to_array(img)
    
    img /= 255
    
    result = []
    for i in img[0]:
        for j in i:
            if j == 0:
                result.append(1)
            else:
                result.append(0)
    return result
    

def print_img(img):
    for i in range(28):
        string = ""
        for j in range(28):
            p = int(img[28*i+j])
            if p == 0:
                string += " "
            else:
                string += str(p)
        print(string)    

        
if __name__ == "__main__":
    pass
