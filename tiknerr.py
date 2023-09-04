import tkinter as tk
from PIL import Image, ImageTk

def display_picture1():
    image_path = "images.jpg"  
    display_image(image_path)

def display_picture2():
    image_path = "download.jpg"   
    display_image(image_path)

def display_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # Keep a reference to prevent garbage collection

# Create the main window
window = tk.Tk()
window.title("Picture Viewer")

# Create labels to display the pictures
label = tk.Label(window)
label.pack()

def exitt():
    return
button5 = tk.Button(window, text= "exit", command=exitt)
# Create buttons to switch between pictures
button1 = tk.Button(window, text="Picture 1", command=display_picture1)
button2 = tk.Button(window, text="Picture 2", command=display_picture2)

button1.pack()
button2.pack()
button5.pack()

window.mainloop()