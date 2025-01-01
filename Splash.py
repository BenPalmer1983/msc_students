import tkinter as tk

class Splash(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("640x480")


        image = tk.PhotoImage(file="splash.png") 
        label = tk.Label(self, image=image)
        label.pack()

        # Show the splash screen for 3000 milliseconds then destroy
        self.after(2000, self.destroy)
        self.mainloop()



    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
