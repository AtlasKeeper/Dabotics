import tkinter as tk
from datetime import datetime, timedelta
import threading
import time
import pygame

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Alarm Clock")
        self.master.configure(bg="black")  # Set the background color to black

        self.label = tk.Label(master, text="Set Alarm Time (HH:MM):", fg="white", bg="black")  # Set text and background color
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, bg="white")  # Set background color of the entry widget
        self.entry.pack(pady=10)

        self.set_button = tk.Button(master, text="Set Alarm", command=self.set_alarm, bg="green", fg="white")  # Set background and text color
        self.set_button.pack(pady=10)

        self.dismiss_button = tk.Button(master, text="Dismiss Alarm", command=self.dismiss_alarm, state=tk.DISABLED, bg="red", fg="white")  # Set background and text color
        self.dismiss_button.pack(pady=10)

        # Initialize Pygame mixer
        pygame.mixer.init()

        self.alarm_time = None
        self.is_alarm_set = False
        self.notification_window = None
        self.alarm_thread = None

    def set_alarm(self):
        try:
            alarm_time_str = self.entry.get()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            current_time = datetime.now().replace(second=0, microsecond=0)

            # If the alarm time is in the past, set it for the next day
            if alarm_time.time() <= current_time.time():
                alarm_time = (datetime.now() + timedelta(days=1)).replace(hour=alarm_time.hour, minute=alarm_time.minute)

            self.alarm_time = alarm_time
            self.is_alarm_set = True

            self.set_button.config(state=tk.DISABLED)
            self.dismiss_button.config(state=tk.NORMAL)

            self.alarm_thread = threading.Thread(target=self.check_alarm)
            self.alarm_thread.start()

        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")

    def check_alarm(self):
        while self.is_alarm_set:
            current_time = datetime.now().replace(second=0, microsecond=0)

            if current_time.time() == self.alarm_time.time():
                self.show_notification()
                self.is_alarm_set = False
                self.set_button.config(state=tk.NORMAL)
                self.dismiss_button.config(state=tk.DISABLED)

            time.sleep(1)

    def play_alarm_sound(self):
        # Load and play the alarm sound
        pygame.mixer.music.load("alarm_sound.mp3")  # Replace with the path to your sound file
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def show_notification(self):
        self.notification_window = tk.Toplevel(self.master)
        self.notification_window.title("Alarm Notification")
        self.notification_window.configure(bg="black")  # Set the background color to black

        label = tk.Label(self.notification_window, text="Time to wake up!", font=("Helvetica", 16), fg="white", bg="black")  # Set text and background color
        label.pack(padx=20, pady=20)

        close_button = tk.Button(self.notification_window, text="Dismiss", command=self.dismiss_notification, bg="red", fg="white")  # Set background and text color
        close_button.pack(pady=10)

        # Play alarm sound
        self.play_alarm_sound()

        # Wait for the notification window to close before continuing
        self.master.wait_window(self.notification_window)

    def dismiss_notification(self):
        if self.notification_window:
            self.notification_window.destroy()

        # Stop the alarm sound
        pygame.mixer.music.stop()

    def dismiss_alarm(self):
        self.is_alarm_set = False
        if self.alarm_thread and self.alarm_thread.is_alive():
            self.alarm_thread.join()  # Wait for the alarm thread to finish
        self.set_button.config(state=tk.NORMAL)
        self.dismiss_button.config(state=tk.DISABLED)
        self.dismiss_notification()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
