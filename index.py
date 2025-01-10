import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

# Global variable to hold the image
img = None

# Function to browse image
def browse():
    global img
    filename = filedialog.askopenfilename(title="Select a File", filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp")])  # Select a file from the system
    if filename:  # Check if a file is selected
        img = Image.open(filename)  # Open the selected file
        messagebox.showinfo("Image Selected", "Image loaded successfully!")

# Function to convert PNG to JPG
def png_to_jpg():
    global img
    if img:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG Image", "*.jpg")])  # Choose the path and change extension to jpg
        if export_file_path:  # Check if a path is selected
            img.convert("RGB").save(export_file_path)  # Save the file in JPG format
            messagebox.showinfo("Conversion Success", "Image successfully converted to JPG!")
        else:
            messagebox.showwarning("No Path Selected", "No file path selected.")
    else:
        messagebox.showerror("No Image Loaded", "Please load an image first.")

# Function to convert JPG to PNG
def jpg_to_png():
    global img
    if img:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG Image", "*.png")])  # Choose the path and change extension to png
        if export_file_path:  # Check if a path is selected
            img.save(export_file_path)  # Save the file in PNG format
            messagebox.showinfo("Conversion Success", "Image successfully converted to PNG!")
        else:
            messagebox.showwarning("No Path Selected", "No file path selected.")
    else:
        messagebox.showerror("No Image Loaded", "Please load an image first.")

# Dictionary to map file formats to their conversion functions
conversion_functions = {
    'png': png_to_jpg,
    'jpg': jpg_to_png
}

# Function to call the appropriate conversion based on selected format
def convert_image(file_format):
    if file_format in conversion_functions:
        conversion_functions[file_format]()  # Call the corresponding function from the dictionary
    else:
        messagebox.showerror("Unsupported Format", "This format is not supported!")

# Create the main window
root = tk.Tk()
root.title("Image Format Converter")
root.geometry('500x300')  # Set window size
root.config(bg='#f0f0f0')  # Set background color

# Create and configure a frame to contain widgets
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Title label
label = tk.Label(frame, text="Image Format Converter", font=("Arial", 18, "bold"), bg='#f0f0f0')
label.pack(pady=20)

# Browse button
browse_button = tk.Button(frame, text="Browse an Image", command=browse, fg="white", bg="#007BFF", font=("Arial", 12), width=20, height=2)
browse_button.pack(pady=10)

# Convert to JPG button
png_to_jpg_button = tk.Button(frame, text="Png to Jpg", command=lambda: convert_image('png'), fg="white", bg="#28A745", font=("Arial", 12), width=20, height=2)
png_to_jpg_button.pack(pady=10)

# Convert to PNG button
jpg_to_png_button = tk.Button(frame, text="Jpg to Png", command=lambda: convert_image('jpg'), fg="white", bg="#FFC107", font=("Arial", 12), width=20, height=2)
jpg_to_png_button.pack(pady=10)

# Start the main loop
root.mainloop()