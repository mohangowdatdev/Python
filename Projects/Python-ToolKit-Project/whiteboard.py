import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Digital Whiteboard")

# Create the canvas where the user can draw
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill='both', expand=True)


# Create the "Clear" button
def clear_canvas():
    canvas.delete("all")


clear_button = tk.Button(window, text="Clear", command=clear_canvas)
clear_button.pack()

# Create the color picker
color_picker = tk.StringVar()
color_picker.set("black")  # default color
color_options = ["black", "red", "green", "blue"]
for color in color_options:
    tk.Radiobutton(window, text=color, variable=color_picker, value=color).pack()


# Bind the left mouse button to a function that draws on the canvas
def draw(event):
    global start_x, start_y
    x, y = event.x, event.y
    if not start_x:
        start_x, start_y = x, y
    color = color_picker.get()
    canvas.create_line(start_x, start_y, x, y, fill=color, width=5)
    start_x, start_y = x, y


def start_drawing(event):
    global start_x, start_y
    start_x, start_y = None, None


canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

# Run the tkinter event loop
window.mainloop()
