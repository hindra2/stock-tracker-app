from calendar import c
import tkinter as tk
from numpy import column_stack
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


# Dropdown Menu Class
class DropDown(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

        self.initUI()
    
    def initUI(self):
        self.menu = tk.Menu(self.frame)
        self.parent.config(menu=self.menu)


        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Option1", command=self.doNothing)
        self.file_menu.add_command(label="Option2", command=self.doNothing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.doNothing)


        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.doNothing)
        self.edit_menu.add_command(label="Redo", command=self.doNothing)

    
    def doNothing(self):
        print("Nothing")



# class Statusbar(tk.Frame):
#     pass


# class Navbar(tk.Frame):
#     pass


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



class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.initUI()
        self.frame.grid(column=1, row=0)

    def initUI(self):
        self.ticker_label = tk.Label(self.frame, text="Ticker: ")
        self.ticker_label.grid(column=0, row=1)

        self.entry_ticker = tk.Entry(self.frame, width=25)
        self.entry_ticker.grid(column=1, row=1)

        self.input_button = tk.Button(self.frame, text="Input", command=self.printInput)
        self.input_button.grid(column=2, row=1)

        self.print_ticker = tk.Label(self.frame, text="")
        self.print_ticker.grid(column=1, row=2)

        self.conclusion_button = tk.Button(self.frame, text="Print Data", command=self.getData)
        self.conclusion_button.grid(column=1, row=3)

        self.print_conclusion = tk.Label(self.frame, text="")
        self.print_conclusion.grid(column=1, row=4)

        self.type_label = tk.Label(self.frame, text="Close/Open/High/Low:")
        self.type_label.grid(column=1, row=5)

        self.plot_type = tk.Entry(self.frame, width=25)
        self.plot_type.grid(column=1, row=6)

        self.plot_button = tk.Button(self.frame, text="Plot History", command=self.plotHistory)
        self.plot_button.grid(column=1, row=7)

    def printInput(self):
        self.input_ticker = self.entry_ticker.get()
        self.print_ticker.config(text=f"Ticker: {self.input_ticker}")
        self.stock = Stock(self.input_ticker)

    def getData(self):
        openingPrice = self.stock.getOpeningPrice()
        priceRange = self.stock.getPriceRange()
        volume = self.stock.getVolume()
        name = self.stock.name
        self.print_conclusion.config(text=f"Name: {name}\nOpening Price:  {openingPrice}\nPrice Range: {priceRange}\nVolume: {volume}")

    def plotHistory(self):
        type = self.plot_type.get()
        graph = self.stock.plotHistory(type)
        canvas = FigureCanvasTkAgg(graph, master=self.parent)
        canvas.get_tk_widget().grid(row=8, column=1)

        toolbar_frame = tk.Frame(master = self.frame)
        toolbar_frame.grid(row=9, column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)

    def closeWindows(self):
        self.parent.destroy()

class MainApp(tk.Frame):
    def __init__(self, parent, title, geometry):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.parent.geometry(geometry)
        self.parent.title(title)

        self.initUI()

    def initUI(self):
        # self.statusbar = Statusbar(self.parent)
        # self.navbar = Navbar(self.parent)
        self.toolbar = Toolbar(self.parent)
        self.dropdown = DropDown(self.parent)
        self.main = MainWindow(self.parent)

def main():
    window = tk.Tk()
    MainApp(window, "StockAppIA", "1920x1080")
    window.mainloop()

if __name__ == "__main__":
    main()