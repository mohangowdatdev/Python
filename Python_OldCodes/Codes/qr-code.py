import qrcode
import tkinter as tk
from PIL import Image, ImageTk


img = qrcode.make(input("Enter Text or URL : "))
img.save("SCAN.png")

# Create the main window
window = tk.Tk()

# Open the image file and convert it to a PhotoImage object
image = Image.open("SCAN.png")
photo = ImageTk.PhotoImage(image)

# Create a label and display the image
label = tk.Label(image=photo)
label.pack()

# Run the Tkinter event loop
window.mainloop()
