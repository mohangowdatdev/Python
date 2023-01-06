import time
import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.seconds = 1500
        self.pomodoro_label = tk.Label(master, text="Pomodoro Timer")
        self.pomodoro_label.pack()

        self.time_label = tk.Label(master, text=self.convert_seconds(self.seconds))
        self.time_label.pack()

        self.clock_label = tk.Label(master, text="")
        self.clock_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.update_clock()

    def start(self):
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.countdown()

    def stop(self):
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def countdown(self):
        if self.seconds > 0:
            self.seconds -= 1
            self.time_label.config(text=self.convert_seconds(self.seconds))
            self.time_label.after(1000, self.countdown)
        else:
            self.time_label.config(text="Time's up!")
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    def convert_seconds(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

root = tk.Tk()
root.title("Pomodoro")
root.geometry("250x120")

app = PomodoroTimer(root)
root.mainloop()
