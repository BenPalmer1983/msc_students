import tkinter as tk

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()