import tkinter as tk
from PIL import Image, ImageTk
import os

def show_image():
    animal = entry.get().lower().strip()
    path = f"animal_images/{animal}.jpg"
    if os.path.exists(path):
        img = Image.open(path).resize((300, 300))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        status_label.config(text=f"This is a {animal.title()}!")
    else:
        status_label.config(text=f"No image found for '{animal}'")
        image_label.config(image="")

# GUI setup
window = tk.Tk()
window.title("Animal Viewer")
window.geometry("400x450")

entry = tk.Entry(window, font=("Helvetica", 12))
entry.pack(pady=10)

button = tk.Button(window, text="Show Animal", command=show_image)
button.pack(pady=5)

status_label = tk.Label(window, text="", font=("Helvetica", 10))
status_label.pack(pady=10)

image_label = tk.Label(window)
image_label.pack()

window.mainloop()