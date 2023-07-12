import tkinter as tk

def increment_counter():
    counter.set(counter.get() + 1)

window = tk.Tk()
window.title("Clicker App")

counter = tk.IntVar()
counter.set(0)

counter_label = tk.Label(window, textvariable=counter, font=("Arial", 24))
counter_label.pack(pady=20)

increment_button = tk.Button(window, text="Click Me", command=increment_counter)
increment_button.pack(pady=10)

window.mainloop()