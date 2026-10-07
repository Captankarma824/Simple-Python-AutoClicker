# Basic auto clicker made in python
import tkinter as tk
import time
import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

root = tk.Tk()
mouse = Controller()

root.title("Auto Clicker")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Auto Clicker", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
tk.Label(root, text="Enter How Many Ticks Per Second", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

entry1 = tk.Entry(root, width=50, font=("Arial", 16), bg="#f0f0f0", justify="center")

tk.Label(root, text ="Use f9 to quit back to menu", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
entry1.pack(pady=20)

running = threading.Event()  


def click_loop(delay):
    while running.is_set():
        mouse.click(Button.left)
        time.sleep(delay)


def start():
    try:
        tps = float(entry1.get())
        if tps <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a number greater than 0")
        return

    running.set()
    root.withdraw()
    threading.Thread(target=click_loop, args=(1.0 / tps,), daemon=True).start()


def stop():
    running.clear()
    root.deiconify()


def on_release(key):
    if key == Key.f9:
        # schedule on the Tkinter thread
        root.after(0, stop)


# Start the listener in the background (non-blocking)
listener = Listener(on_release=on_release)
listener.daemon = True
listener.start()

tk.Button(root, width=10, height=20, text="Start", font=("Ariel", 20), command=start).pack(pady=10)

root.mainloop()