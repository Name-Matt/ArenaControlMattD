import tkinter as tk
import time

def update_label():
    # get the current time in seconds with high resolution
    now = time.perf_counter()
    # calculate the time elapsed since the start
    elapsed_time = now - start_time
    label.config(text='Time elapsed: {:.2f} sec'.format(elapsed_time))
    # schedule the update_label() function to be called again after 1 milliseconds
    root.after(1, update_label)

root = tk.Tk()
label = tk.Label(root, text='Starting')
label.pack()
# get the start time
start_time = time.perf_counter()
# schedule the update_label() function to be called after 1 milliseconds
root.after(1, update_label)
root.mainloop()
