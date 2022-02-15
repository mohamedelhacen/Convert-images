from PIL import Image
import sys
import os
import tkinter as tk
from tkinter import filedialog

rt = tk.Tk()
font = ('helvetica', 12, 'bold')
bg = 'blue'
fg = 'black'
width = 15

def getImagePath():
    global imgPath
    imgPath = filedialog.askopenfilenames()

def convert_imgs():
    print('converting...')
    img = None
    i = 0
    j = 0
    for filename in imgPath:
        if filename.endswith(".jpg"):
            img = Image.open(filename).convert("RGB")
            img.save(filename.replace("jpg", "png"), "png")
            i += 1
        elif filename.endswith('.png'):
            img = Image.open(filename).convert("RGB")
            img.save(filename.replace('png', 'jpg'), 'jpeg')
            j += 1
        else:
            continue
    message = f'''Converting...
            Converting {i} image(s) from jpg to png 
            Converting {j} image(s) from png to jpeg
End of conversion.'''
    canvas1.create_text(250, 250, text=message, fill="green", font=('helvetica', 14, 'bold'))

rt.title("Image converter")
canvas1 = tk.Canvas(rt, width=500, height=350, bg='lightblue')
canvas1.pack()

label1 = tk.Label(rt, text="Convert PNG images to JPEG images and vice versa", bg='lightblue')
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 50, window=label1)

browseButton = tk.Button(text='Browse to images', command=getImagePath, bg=bg, fg=fg, font=font, width=width)
canvas1.create_window(250, 150, window=browseButton)

outputButton = tk.Button(text="Convert images", command=convert_imgs, bg=bg, fg=fg, font=font, width=width)
canvas1.create_window(250, 200, window=outputButton)


rt.mainloop()
