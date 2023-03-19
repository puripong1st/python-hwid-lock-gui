from pathlib import Path
from tkinter import Tk, Canvas, END, Text, Button, PhotoImage,messagebox
import requests
import subprocess
import pyperclip


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".img\\")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
datahwid =requests.get("https://pastebin.com/raw/AsmGzNHk")

def create_widgets():
    global textbox
    textbox = Text(window, state='disabled')
    textbox.pack()
    textbox.config(height=1, width=40, font=("Inter", 22 * -1), state='normal')
    textbox.insert(END, f"{hwid}\n")
    textbox.place(x=10, y=385)
    textbox.config(bg='#ffffff')
    textbox.bind("<Key>", lambda e: "break")

def copy_text():
    text = textbox.get("1.0", END).strip()
    pyperclip.copy(text)
    messagebox.showinfo("Lock HWID BY PRP", "คัดลอก HWID เสร็จสิ้น !")    

def go_to_window_2():
    global window_2
    window.destroy()
    window_2 = Tk()
    window_2.geometry("600x651")
    window_2.configure(bg = "#FFFFFF")

    canvas_2 = Canvas(
        window_2,
        bg = "#FFFFFF",
        height = 651,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_2.place(x = 0, y = 0)
   
    canvas_2.create_text(
        165.0,
        336.0,
        anchor="nw",
        text="ยินดีด้วยเข้าโปรแกรมได้แล้ว",
        fill="#FF0000",
        font=("Inter ExtraBold", 32 * -1)
)
    window_2.resizable(False, False)
    window_2.mainloop()

def Main_Program():
    if hwid in datahwid.text:
        print("Login true")
        messagebox.showinfo("Login Successful", "Welcome to the program!")
        window.after(500, go_to_window_2)
    else:
        print("Login faill")
        print(hwid)
        messagebox.showerror("Login Failed", "Invalid HWID")

def exit():
    window.destroy()

window = Tk()

window.config(bg = "#FFFFFF")
width_of_window = 500
height_of_window = 700
labels = []  
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
window.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
window.overrideredirect(1) 
window.resizable(False, False)   
window.attributes('-topmost', 1)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    250.0,
    121.0,
    image=image_image_1
)

create_widgets()

canvas.create_text(
    10.0,
    352.0,
    anchor="nw",
    text="HWID",
    fill="#000000",
    font=("Inter", 23 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=copy_text,
    relief="flat"
)
button_1.place(
    x=405.0,
    y=424.0,
    width=86.0,
    height=26.0
)

canvas.create_text(
    185.0,
    246.0,
    anchor="nw",
    text="Name SHOP",
    fill="#000000",
    font=("Inter", 23 * -1)
)
canvas.create_text(
    128.0,
    276.0,
    anchor="nw",
    text="PROJECT : TEST FREE",
    fill="#000000",
    font=("Inter", 23 * -1)
)
canvas.create_text(
    185.0,
    306.0,
    anchor="nw",
    text="VERSION : 1",
    fill="#000000",
    font=("Inter", 23 * -1)
)

canvas.create_text(
    415.0,
    685.0,
    anchor="nw",
    text="License : PRP",
    fill="#000000",
    font=("Inter", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Main_Program,
    relief="flat"
)
button_2.place(
    x=122.0,
    y=517.0,
    width=256.0,
    height=67.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=exit,
    relief="flat"
)
button_3.place(
    x=122.0,
    y=616.0,
    width=256.0,
    height=67.0
)
window.resizable(False, False)
window.mainloop()
