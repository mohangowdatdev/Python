import qrcode as qr
import tkinter as tk
from PIL import Image, ImageTk
import sys

while True:
    print("-------------------------------------------")
    print("Enter URL / Text (type 'exit' to exit) : \n")
    feed = input("> ")
    if feed == "exit":
        sys.exit()
    img = qr.make(feed)
    img.save("qr.png")

    # Create the main window
    window = tk.Tk()

    # Open the image file and convert it to a PhotoImage object
    image = Image.open("qr.png")
    photo = ImageTk.PhotoImage(image)

    # Create a label and display the image
    label = tk.Label(image=photo)
    label.pack()

    # Run the Tkinter event loop
    window.mainloop()
