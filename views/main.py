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
window_title = "PAINT UP"
window.title(window_title)
actions = True
canvas_width = 595
canvas_height = 419

window.geometry("600x500")
window.configure(bg = "#FFFFFF")

img = np.ones((canvas_height, canvas_width, 3), dtype = np.uint8)*255
temp_img = img.copy()
color = (0, 0, 0)
brush = ["circle", 3]


def get_radious(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)


def create_widgets():
    global paint_img

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


    img_pil = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(img_pil)
    paint_img = tk.Label(window, image=img_tk)
    paint_img.place(x=0, y=76)

    window.resizable(False, False)
    window.bind("<B1-Motion>", draw)
    window.bind("<ButtonRelease-1>", last_position)
    window.mainloop()
    

def update_image():
    global img, temp_img, img_tk, paint_img
    
    img_pil = Image.fromarray(temp_img)
    img_tk = ImageTk.PhotoImage(img_pil)
    paint_img.config(image=img_tk)


def last_position(event):
    global actions, x2, y2, img, temp_img

    x = event.x
    y = event.y
    img = temp_img
    actions = True
    x2 = x
    y2 = y

def draw(event):    
    global actions, x1, x2, y1, y2, ix, iy, img, temp_img

    x = event.x
    y = event.y

    if actions:
        actions = False
        x1, y1 = x, y
        ix, iy = x, y

    if brush[0] == 'circle':
        temp_img = img.copy()
        x2, y2, = x, y
        radious = get_radious(x1, y1, x2, y2)
        cv2.circle(temp_img, (x1, y1), int(radious), color, 2, lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'rectangle':
        temp_img = img.copy()
        cv2.rectangle(temp_img, (x1, y1), (x, y), color, 2, lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'pencil':
        temp_img = img.copy()
        cv2.line(img, (ix, iy), (x, y), color, thickness=2, lineType=cv2.LINE_AA)
        ix, iy = x, y
        update_image()
    if brush[0] == 'line':
        temp_img = img.copy()
        cv2.line(temp_img, (x1, y1), (x, y), color, thickness=2, lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'eraser':
        cv2.circle(temp_img, (x, y), 20, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        update_image()


def rgb_to_bgr(rgb):
    r, g, b = rgb
    return b, g, r

def change_color():
    global color

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
    global temp_img
    temp_img = 255*np.ones((600, 800, 3), dtype = np.uint8)
    update_image()


create_widgets()
