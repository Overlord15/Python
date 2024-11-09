import tkinter as tk
from tkinter import filedialog
from PIL import Image
import concurrent.futures

def resize_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        img = img.resize((width, height), Image.LANCZOS)
        img.save(output_path)

def resize_image_thread(input_path, output_path, width, height):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(resize_image, input_path, output_path, width, height)
        return future.result()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg;*.jpeg")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def start_resize():
    input_path = input_entry.get()
    output_path = output_entry.get()
    width = int(width_entry.get())
    height = int(height_entry.get())
    resize_image_thread(input_path, output_path, width, height)
    result_label.config(text="Image resized successfully!")

app = tk.Tk()
app.title("Image Resizer")

tk.Label(app, text="Input Image:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(app, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Output Image:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(app, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_save_file).grid(row=1, column=2, padx=10, pady=10)

tk.Label(app, text="Width:").grid(row=2, column=0, padx=10, pady=10)
width_entry = tk.Entry(app, width=10)
width_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Label(app, text="Height:").grid(row=3, column=0, padx=10, pady=10)
height_entry = tk.Entry(app, width=10)
height_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Button(app, text="Resize", command=start_resize).grid(row=4, column=1, padx=10, pady=10, sticky="e")
result_label = tk.Label(app, text="")
result_label.grid(row=5, column=1, padx=10, pady=10)

app.mainloop()
