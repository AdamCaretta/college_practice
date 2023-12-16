import tkinter as tk
from tkinter import ttk
import datetime


class ListWindow:
    def __init__(self, items):
        self.root = tk.Tk()
        self.root.geometry("500x300")

        self.root.title("Scrollbar box thing")

        self.add_button = ttk.Button(
            self.root,
            text="Add Item",
            command=lambda: self.add_item(datetime.datetime.now()),
        ).pack()

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.listNodes = tk.Listbox(
            self.frame, width=20, height=20, font=("Helvetica", 14)
        )
        self.listNodes.pack(side="left", fill="y")
        self.listNodes.bind('<<ListboxSelect>>', self.on_selection)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.listNodes.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listNodes.config(yscrollcommand=self.scrollbar.set)

        for item in items:
            self.add_item(item)

    
    def on_selection(self, event):
        widget = event.widget
        item = widget.curselection()
        value = widget.get(item[0])
        print(f'Selected Value: {value}')




    
    def add_item(self, item):
        self.listNodes.insert(tk.END, str(item))


items = ["apples", "taco", "potato", "grape"]

listWindow = ListWindow(items)
listWindow.root.mainloop()
