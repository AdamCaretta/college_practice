import tkinter as tk
from tkinter import ttk


def show_hello(event=None):
    first_name = first_entry.get()
    last_name = last_entry.get()

    print(f"Hello, {first_name} {last_name}")


root = tk.Tk()
root.title('Event Listener Example')
root.bind('<Return>', show_hello)

container = ttk.Frame(root)

first_label = ttk.Label(container, text="First Name:")
last_label = ttk.Label(container, text="Last Name:")

first_entry = ttk.Entry(container)
last_entry = ttk.Entry(container)


quit_button = ttk.Button(container, text="Quit", command=quit)
show_button = ttk.Button(container, text="Show", command=show_hello)

container.grid(column=0, row=0)
first_label.grid(column=0, row=0)
first_entry.grid(column=1, row=0)
last_label.grid(column=0, row=1)
last_entry.grid(column=1, row=1)
quit_button.grid(column=0, row=2)
show_button.grid(column=1, row=2)


root.mainloop()
