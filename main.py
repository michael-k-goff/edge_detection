import numpy as np
import cv2
from tkinter import *
from PIL import ImageTk
from PIL import Image

master = Tk()
master.title("Edge Detection")

display_params = {
    "min":100,
    "max":200,
    "algo":"canny"
}

# Cat picture
kitty = cv2.cvtColor(cv2.imread("kitty.jpeg"), cv2.COLOR_BGR2RGB)
kitty = cv2.resize(kitty, (450,600), interpolation = cv2.INTER_AREA)

def dashboard():
    full_img = 255*np.ones([100+kitty.shape[0],2*kitty.shape[1],3 ], dtype=np.uint8)
    
    cv2.rectangle(
        full_img,
        (50,kitty.shape[0]+45),
        (700,kitty.shape[0]+60),
        (0, 0, 0),
        thickness=15,
        lineType=cv2.LINE_8
    )
    
    pts = np.array([[display_params["max"]+48,605],[display_params["max"]+52,605],[display_params["max"]+50,628]], np.int32)
    cv2.polylines(full_img,[pts],True,(0,0,0), thickness=4)
    
    pts = np.array([[display_params["min"]+48,695],[display_params["min"]+52,695],[display_params["min"]+50,672]], np.int32)
    cv2.polylines(full_img,[pts],True,(0,0,0), thickness=4)
    return full_img

# Canvas
canvas_height, canvas_width, no_channels = kitty.shape
w = Canvas(master, 
           width=2*kitty.shape[1],
           height=100+kitty.shape[0])
w.pack()

def make_image():
    # Exposition of canny edge detection here: https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
    # 100, 200 were the given minVal, maxVal values.
    edges = cv2.Canny(kitty,display_params["min"],display_params["max"])
    full_img = dashboard()
    
    # Convert the Image objects into a TkPhoto object
    im_full = Image.fromarray(full_img)
    imgtk_full = ImageTk.PhotoImage(image=im_full)
    label = Label(image=imgtk_full)
    label.image = imgtk_full

    im = Image.fromarray(kitty)
    imgtk = ImageTk.PhotoImage(image=im)
    label = Label(image=imgtk)
    label.image = imgtk

    im2 = Image.fromarray(edges)
    imgtk2 = ImageTk.PhotoImage(image=im2)
    label = Label(image=imgtk2)
    label.image = imgtk2

    # Put the images in the display window
    image_id = w.create_image(0, 0, image=imgtk_full, anchor=NW)
    image_id = w.create_image(0, 0, image=imgtk, anchor=NW)
    image_id = w.create_image(450, 0, image=imgtk2, anchor=NW)
make_image()

def mouse_click(event):
    x=event.x;
    y=event.y;
    if (y >= kitty.shape[0] and y < kitty.shape[0]+50 and x >= 50 and x < 700):
        display_params["max"] = x-50;
        if display_params["max"] < display_params["min"]:
            display_params["max"] = display_params["min"]
    if (y >= kitty.shape[0]+50 and x >= 50 and x < 700):
        display_params["min"] = x-50;
        if display_params["max"] < display_params["min"]:
            display_params["min"] = display_params["max"]
    make_image()
    
master.bind("<Button-1>", mouse_click)

mainloop()