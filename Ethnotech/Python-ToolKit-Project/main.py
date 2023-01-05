import tkinter as tk
import subprocess

class Menu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text="Notepad 🗒️", width=25, command=self.run_script1)
        self.button2 = tk.Button(self.frame, text="Whiteboard 🔳", width=25, command=self.run_script2)
        self.button3 = tk.Button(self.frame, text="QR Code 📱", width=25, command=self.run_script3)
        self.button4 = tk.Button(self.frame, text="Timer ⏱️", width=25, command=self.run_script4)
        self.button1.pack(pady=4)
        self.button2.pack(pady=4)
        self.button3.pack(pady=4)
        self.button4.pack(pady=4)
        self.frame.pack()

    def run_script1(self):
        subprocess.call(["python", "notepad.py"])

    def run_script2(self):
        subprocess.call(["python", "whiteboard.py"])

    def run_script3(self):
        subprocess.call(["python", "qr-code.py"])

    def run_script4(self):
        subprocess.call(["python", "work-timer.py"])

root = tk.Tk()
root.title("Home")
root.geometry("250x140")
app = Menu(root)
root.mainloop()
