import tkinter as tk

# Creating a window to type
window = tk.Tk()
window.title("NOTEPAD")

# Creating a frame to place textpad and scrollbar
frame = tk.Frame(window)

# To enter text and sync it with scrollbar
text = tk.Text(frame, wrap='word', font=("Courier New", 16))
scrollbar = tk.Scrollbar(window, orient="vertical", command=text.yview)
text.configure(yscrollcommand=scrollbar.set)

# Packing tools
text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
frame.pack(fill='both', expand=True)


# To create the saving function
def saving():
    text_wid = text.get("1.0", "end-1c")
    with open("notepad.txt", "w") as f:
        f.write(text_wid)


# Save button creation
save = tk.Button(window, text="Save", width=9, bg='gray', fg='white', font=("Arial", 10), command=saving)
save.pack(side="left", fill='none', padx=10)


# clear function creation
def on_clear_button_clicked():
    # Clear the text from the text widget
    text.delete('1.0', 'end')


# Clear button creation
clear_button = tk.Button(window, text="Clear", width=9, bg='red', fg='white', font=("Arial", 10))
clear_button.pack(side="left", fill='none', padx=4)

# Set the command to be executed when the clear button is clicked
clear_button.configure(command=on_clear_button_clicked)

# To run the loop
window.mainloop()
