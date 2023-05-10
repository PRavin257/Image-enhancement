
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
from tkinter import filedialog
import numpy as np
import os



def displayimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage



def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)

    global outputImage
    enhancer = ImageEnhance.Brightness(img)
    outputImage = enhancer.enhance(brightness_pos)
    displayimage(outputImage)



def sharpen_callback(sharpness_pos):
    sharpness_pos = float(sharpness_pos)
   
    global outputImage
    enhancer = ImageEnhance.Sharpness(img)
    outputImage = enhancer.enhance(sharpness_pos)
    displayimage(outputImage)



def rotate():
    global img
    img = img.rotate(90)
    displayimage(img)



def flip():
    global img
    img = img.transpose((Image.FLIP_LEFT_RIGHT))
    displayimage(img)



def blurr():
    global img
    img = img.filter(ImageFilter.BLUR)
    displayimage(img)


def edgeEnhance():
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)


def ChangeImg():
    global img
    imgname = filedialog.askopenfilename(title="Change Image")
    if imgname:
        img = Image.open(imgname)
        img = img.resize((600, 600))
        displayimage(img)

def close():
    mains.destroy()


mains = Tk()
space=(" ")*215
screen_width=mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()

#mains.geometry("1000x700")
mains.geometry(f"{screen_width}x{screen_height}")
mains.title(f"{space}Image Editor")
mains.configure(bg='white')


# <------Default image in editor------>
img = Image.open("image.jpg")
img = img.resize((700, 600))

# <------Creating panel to display image------>
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)




brightnessSlider = Scale(mains, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,
                         resolution=0.1, command=brightness_callback, bg="Grey")
brightnessSlider.set(1)
brightnessSlider.configure(font=('Times new roman',11,'bold'),foreground='black')
brightnessSlider.place(x=1050,y=500)




sharpnessSlider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        command=sharpen_callback, resolution=0.1, bg="Grey")
sharpnessSlider.set(1)
sharpnessSlider.configure(font=('Times new roman',11,'bold'),foreground='black')
sharpnessSlider.place(x=800,y=500)




btnRotate = Button(mains, text='Rotate', width=25, command=rotate, bg="Black")
btnRotate.configure(font=('Times new roman',12,'bold'),foreground='white')
btnRotate.place(x=300,y=700)



btnChaImg = Button(mains, text='Change Image', width=25,command=ChangeImg,bg="White",activebackground="blue")
btnChaImg.configure(font=('Times new roman',12,'bold'),foreground='Black')
btnChaImg.place(x=50,y=700)



btnFlip = Button(mains, text='Flip', width=25, command=flip, bg="Black")
btnFlip.configure(font=('Times new roman',12,'bold'),foreground='white')
btnFlip.place(x=550,y=700)



btnBlur = Button(mains, text='Blur', width=25, command=blurr, bg="Black")
btnBlur.configure(font=('Times new roman',12,'bold'),foreground='white')
btnBlur.place(x=800,y=700)


btnEdgeEnhance = Button(mains, text='EdgeEnhance', width=25, command=edgeEnhance, bg="Black")
btnEdgeEnhance.configure(font=('Times new roman',12,'bold'),foreground='white')
btnEdgeEnhance.place(x=1050,y=700)


btnClose = Button(mains, text='Close', command=close, bg="Red",activebackground="Blue")
btnClose.configure(font=('Times new roman',12,'bold'),foreground='white')
btnClose.place(x=1400,y=700)

mains.mainloop()
