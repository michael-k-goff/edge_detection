import numpy as np
import cv2
from tkinter import *
from PIL import ImageTk
from PIL import Image
import math

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
# See the following for some code snippets on the Sobel filter.
# https://gist.github.com/rahit/c078cabc0a48f2570028bff397a9e154
gray_kitty = cv2.cvtColor(kitty, cv2.COLOR_BGR2GRAY)
gaussian_kitty = cv2.GaussianBlur(gray_kitty,(3,3),0)

def dashboard():
    full_img = 255*np.ones([100,2*kitty.shape[1],3 ], dtype=np.uint8)
    
    cv2.rectangle(
        full_img,
        (50,45),
        (700,60),
        (0, 0, 0),
        thickness=15,
        lineType=cv2.LINE_8
    )
    
    pts = np.array([[display_params["max"]+48,5],[display_params["max"]+52,5],[display_params["max"]+50,28]], np.int32)
    cv2.polylines(full_img,[pts],True,(0,0,0), thickness=4)
    
    pts = np.array([[display_params["min"]+48,95],[display_params["min"]+52,95],[display_params["min"]+50,72]], np.int32)
    cv2.polylines(full_img,[pts],True,(0,0,0), thickness=4)
    
    if display_params["algo"]=="canny":
        cv2.putText(full_img, "Canny", (710, 30), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,0,0), 1, cv2.LINE_AA)
    else:
        cv2.putText(full_img, "Canny", (710, 30), cv2.FONT_HERSHEY_PLAIN, 1.3, (0,0,0), 1, cv2.LINE_AA)
    if display_params["algo"]=="sobel":
        cv2.putText(full_img, "Sobel", (800, 30), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,0,0), 1, cv2.LINE_AA)
    else:
        cv2.putText(full_img, "Sobel", (800, 30), cv2.FONT_HERSHEY_PLAIN, 1.3, (0,0,0), 1, cv2.LINE_AA)
    return full_img

# Canvas
canvas_height, canvas_width, no_channels = kitty.shape
w = Canvas(master, 
           width=2*kitty.shape[1],
           height=100+kitty.shape[0])
w.pack()

def edge_detection():
    if display_params["algo"] == "canny":
        return cv2.Canny(kitty,display_params["min"],display_params["max"])
    else:
        # A decent explanation of Sobel filters, including the kernel. https://www.cs.auckland.ac.nz/compsci373s1c/PatricesLectures/Edge%20detection-Sobel_2up.pdf
        base_val = math.floor(display_params["max"]*4/650)
        img_sobelx = cv2.Sobel(gaussian_kitty,cv2.CV_8U,1,0,ksize=1+2*base_val)
        img_sobely = cv2.Sobel(gaussian_kitty,cv2.CV_8U,0,1,ksize=1+2*base_val)
        return (img_sobelx + img_sobely)

def make_image():
    # Exposition of canny edge detection here: https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
    # 100, 200 were the given minVal, maxVal values.
    edges = edge_detection()
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
    image_id = w.create_image(0, kitty.shape[0], image=imgtk_full, anchor=NW) # Dashboard
    image_id = w.create_image(0, 0, image=imgtk, anchor=NW) # Original picture
    image_id = w.create_image(kitty.shape[1], 0, image=imgtk2, anchor=NW) # Showing the edge detection
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
    if (x >= 700):
        if x<780 and y < 50+kitty.shape[0]:
            display_params["algo"] = "canny"
        if x>=780 and y < 50+kitty.shape[0]:
            display_params["algo"] = "sobel"
    make_image()
    
master.bind("<Button-1>", mouse_click)

mainloop()