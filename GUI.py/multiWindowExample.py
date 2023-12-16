import tkinter as tk
from tkinter import ttk

"""
def show_hello(event=None):
    first_name = first_entry.get()
    last_name = last_entry.get()

    print(f"Hello, {first_name} {last_name}")
"""


class InputWindow:
    def __init__(self, root, name_list):
        # root = tk.Tk()
        # root.title("Event Listener Example")
        # root.bind("<Return>", show_hello)

        self.container = ttk.Frame(root)

        first_label = ttk.Label(self.container, text="First Name:")
        last_label = ttk.Label(self.container, text="Last Name:")

        first_entry = ttk.Entry(self.container)
        last_entry = ttk.Entry(self.container)

        quit_button = ttk.Button(self.container, text="Quit", command=quit)
        add_button = ttk.Button(
            self.container,
            text="Add",
            command=lambda: self.add_to_list(first_entry.get(), last_entry.get()),
        )
        list_button = ttk.Button(
            self.container, text="List", command=self.go_to_list_window
        )

        self.container.grid(column=0, row=0, sticky="news")
        first_label.grid(column=0, row=0)
        first_entry.grid(column=1, row=0, columnspan=2)
        last_label.grid(column=0, row=1)
        last_entry.grid(column=1, row=1, columnspan=2)
        quit_button.grid(column=0, row=2)
        add_button.grid(column=1, row=2)
        list_button.grid(column=2, row=2)

        self.name_list = name_list

    def add_to_list(self, first, last):
        name = " ".join((first, last))

    def go_to_list_window(self):
        self.list_window.show()

    def set_list_window(self, window):
        self.list_window = window

    def show(self):
        self.container.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")

    inputList = []

    InputWindow = InputWindow(root, inputList)

    InputWindow.container.tkraise()

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()
