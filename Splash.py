

import tkinter as tk

class Splash(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("640x480")

        # Load the splash image
        image = tk.PhotoImage(file="splash.png") 
        label = tk.Label(self, image=image)
        label.pack()

        # Show splash screen
        self.after(2000, self.destroy)
        self.mainloop()


