import cv2
import numpy as np
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, messagebox, Tk, Canvas, PhotoImage, Button, Entry
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window_title = "PAINT UP"
window.title(window_title)
actions = True
canvas_width = 894
canvas_height = 562
image_fill_state = False

window.geometry("899x643")
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
        height = 643,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        449.0,
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
        x=83.0,
        y=13.0,
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
        x=17.0,
        y=13.92547607421875,
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
        x=148.80796813964844,
        y=13.0,
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
        x=214.61593627929688,
        y=13.0,
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
        x=280.4239196777344,
        y=13.0,
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
        x=346.23187255859375,
        y=13.0,
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
        x=412.0,
        y=13.92547607421875,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=save_draw,
        relief="flat"
    )
    button_8.place(
        x=478.0,
        y=13.92547607421875,
        width=48.15217208862305,
        height=48.15217208862305
    )

    button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))

    def fill_figures():
        global image_fill_state
        
        if not image_fill_state:
            button_9.configure(image=button_image_10)
            image_fill_state = True
            brush[1] = -1
        else:
            button_9.configure(image=button_image_9)
            image_fill_state = False
            brush[1] = 3


    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=fill_figures,
        relief="flat"
    )
    button_9.place(
        x=544.0,
        y=14.0,
        width=48.15217208862305,
        height=48.15217208862305
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        860.0,
        37.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        761.0,
        38.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        676.0,
        44.0,
        image=image_image_4
    )

    def save_entry_value(event):
        if entry_1.get() and int(entry_1.get()) > 0:
            try:
                brush[1] = int(entry_1.get())
            except:
                messagebox.showinfo("Alerta", "El valor de tamaño de pincel no es un valor valido")
        else:
            messagebox.showinfo("Alerta", "El valor de tamaño de pincel no es un valor valido")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        761.0,
        38.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Comic Sans MS', 12, 'normal')
    )
    entry_1.place(
        x=735.0,
        y=24.0,
        width=52.0,
        height=26.0
    )

    entry_1.bind("<Return>", save_entry_value)

    img_pil = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(img_pil)
    paint_img = tk.Label(window, image=img_tk)
    paint_img.place(x=0, y=76)

    window.resizable(False, False)
    window.bind("<B1-Motion>", draw)
    window.bind("<ButtonRelease-1>", last_position)
    window.mainloop()
    

def update_image():
    global img, temp_img, img_tk, paint_img, img_pil
    
    img_pil = Image.fromarray(temp_img)
    img_tk = ImageTk.PhotoImage(img_pil)
    paint_img.config(image=img_tk)


def last_position(event):
    global actions, img, temp_img
    img = temp_img
    actions = True

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
        cv2.circle(temp_img, (x1, y1), int(radious), color, brush[1], lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'rectangle':
        temp_img = img.copy()
        cv2.rectangle(temp_img, (x1, y1), (x, y), color, brush[1], lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'pencil':
        thick = 3 if brush[1] < 0 else brush[1]
        temp_img = img.copy()
        cv2.line(img, (ix, iy), (x, y), color, thickness=thick, lineType=cv2.LINE_AA)
        ix, iy = x, y
        update_image()
    if brush[0] == 'line':
        thick = 3 if brush[1] < 0 else brush[1]
        temp_img = img.copy()
        cv2.line(temp_img, (x1, y1), (x, y), color, thickness=thick, lineType=cv2.LINE_AA)
        update_image()
    if brush[0] == 'eraser':
        thick = 3 if brush[1] < 0 else brush[1]
        temp_img = img.copy()
        cv2.line(img, (ix, iy), (x, y), (255, 255, 255), thickness=thick, lineType=cv2.LINE_AA)
        ix, iy = x, y
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
    temp_img = 255*np.ones((canvas_height, canvas_width, 3), dtype = np.uint8)
    update_image()


def save_draw():
    global img_pil

    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])
    
    if file_name:
        img_pil.save(file_name)
        print("Imagen guardada exitosamente en:", file_name)


create_widgets()
