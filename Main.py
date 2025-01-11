import tkinter as tk
from App import App
from Splash import Splash


# Main entry point to the program
def main():

    # Create a splash screen
    splash = Splash()

    # Create instance of the app and run it
    app = App()
    app.mainloop()


# Run main
if(__name__ == "__main__"):
    main()