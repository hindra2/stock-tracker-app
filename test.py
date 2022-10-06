from sys import _xoptions
import tkinter as tk

class Toolbar(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg="blue")

        self.initUI()
    
    def initUI(self):
        self.insert_thing = tk.Button(self.frame, text="Insert Thing", command=self.doNothing)
        self.insert_thing.grid(row=0, column=0)
        
        self.print_thing = tk.Button(self.frame, text="Print Thing", command=self.doNothing)
        self.print_thing.grid(row=1, column=0)

        self.frame.grid(row=0, column=0)
        
    def doNothing(self):
        print("ASD")

class Window(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

        self.initUI()

    def initUI(self):
        self.label = tk.Label(text="Hello World")
        self.label.grid(row=0, column=1)

class Main(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

        self.initUI()

    def initUI(self):
        self.toolbar = Toolbar(self.parent)
        self.mainWindow = Window(self.parent)


def main():
    window = tk.Tk()
    Main(window)
    window.mainloop()

if __name__ == "__main__":
    main()