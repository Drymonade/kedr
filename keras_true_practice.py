'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras.preprocessing.image import img_to_array, load_img

from tkinter import *

from PIL import Image as image


class Paint(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)
         self.parent = parent
         self.setUI()
    
    def setUI(self):
 
        self.parent.title("Digit Recognizer!")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне
 
        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        
        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6)               
                       
        self.canv.bind("<B1-Motion>", self.draw)
        btn = Button(self, text="Recognize", width=10, command=self.recognize())
        btn.grid(row=0, column=0)
 
        lab1 = Label(self, text="Answer: ") # Создаем метку для кнопок изменения размера кисти
        lab1.grid(row=3, column=0, padx=5)
    
        answer_lab = Label(self) # Создаем метку для кнопок изменения размера кисти
        answer_lab.grid(row=3, column=1, padx=5)
    
        
    def draw(self, event):
        self.canv.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2,
                              fill="black", outline="black")    
    
        
    def recognize(self):
        self.canv.postscript(file="tmp_canvas.eps",
                             colormode="color",
                             width=28,
                             height=28,
                             pagewidth=27,
                             pageheight=27)
        
        data = image.open("tmp_canvas.eps")
        data.save("canvas_image.png")
        
        img = preprocess_img("canvas_image.png")
        model = load_model("my_model.h5") 
        result = model.predict(img)
        
        self.answer_lab.text = str(max_index(result))
    

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

        
def main():
    root = Tk()
    root.geometry("400x350")
    app = Paint(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()

    
    # img = preprocess_img("3.png")
# print_img(img)
# print(model.predict(np.array([img])))