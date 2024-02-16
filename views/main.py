import cv2
import numpy as np
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, Tk, Canvas, PhotoImage, Button
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
wintow_title = "PAINT UP"
actions = True
canvas_width = 600
canvas_height = 500

window.geometry("600x500")
window.configure(bg = "#FFFFFF")

img = 255*np.ones((canvas_height, canvas_width, 3), dtype = np.uint8)
temp_img = img.copy()
color = (0, 0, 0)
brush = ["pencil", 3]


def create_widgets():
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 500,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    
    image_1 = canvas.create_image(
        300.0,
        38.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=change_to_pencil,
        relief="flat"
    )
    button_1.place(
        x=112.0,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=change_color,
        relief="flat"
    )
    button_2.place(
        x=46.0,
        y=14.0,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=change_to_line,
        relief="flat"
    )
    button_3.place(
        x=177.80796813964844,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=change_to_rectangle,
        relief="flat"
    )
    button_4.place(
        x=243.61593627929688,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=change_to_circle,
        relief="flat"
    )
    button_5.place(
        x=309.4239196777344,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=change_to_eraser,
        relief="flat"
    )
    button_6.place(
        x=375.23187255859375,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=delete_draw,
        relief="flat"
    )
    button_7.place(
        x=441.03985595703125,
        y=13.07452392578125,
        width=48.15217208862305,
        height=48.15217208862305
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        531.0,
        37.0,
        image=image_image_2
    )

    window.resizable(False, False)
    window.mainloop()

def rgb_to_bgr(rgb):
    r, g, b = rgb
    return b, g, r

def change_color():
    color_changed = colorchooser.askcolor()
    if color_changed:
        color = tuple(map(int, color_changed[0]))
        print(rgb_to_bgr(color))

def change_to_pencil():
    brush[0] = 'pencil'
    print(brush[0])


def change_to_line():
    brush[0] = 'line'
    print(brush[0])


def change_to_rectangle():
    brush[0] = 'rectangle'
    print(brush[0])


def change_to_circle():
    brush[0] = 'circle'
    print(brush[0])


def change_to_eraser():
    brush[0] = 'eraser'
    print(brush[0])


def delete_draw():
    img = 255*np.ones((600, 800, 3), dtype = np.uint8)
    print("Draw deleted")


create_widgets()
