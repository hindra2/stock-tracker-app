from doctest import master
from random import weibullvariate
from textwrap import fill
import tkinter as tk
from turtle import width
import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

ui_path = "./assets/icons/"

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")

# class Statusbar(tk.Frame):
#     pass


# class Navbar(tk.Frame):
#     pass


class Toolbar(ctk.CTk):
    def __init__(self, frame):
        super(). __init__()
        self.frame = frame

        self.initImage()
        self.initUI()
    
    def initImage(self):
        self.home = tk.PhotoImage(file=f"{ui_path}home.png")
        self.globe = tk.PhotoImage(file=f"{ui_path}globe.png")
    
    def initUI(self):
        self.insert_thing = ctk.CTkButton(master=self.frame, text="", image=self.home, fg_color=("white", "grey"), command=self.doNothing, width=60, corner_radius=6)
        self.insert_thing.grid(row=0, column=0, padx=5, pady=5)
        
        self.print_thing = ctk.CTkButton(master=self.frame, text="", image=self.globe, fg_color=("white", "grey"), command=self.doNothing, width=60, corner_radius=6)
        self.print_thing.grid(row=1, column=0, padx=5, pady=5)
        
    def doNothing(self):
        print("ASD")



class MainWindow(ctk.CTk):
    def __init__(self, frame, frame2):
        self.frame = frame
        self.frame2 = frame2
        self.initUI()

    def initUI(self):
        self.ticker_label = ctk.CTkLabel(master=self.frame, 
                                        text="Ticker: ", 
                                        corner_radius=21, 
                                        justify=tk.CENTER)
        self.ticker_label.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.entry_ticker = ctk.CTkEntry(master=self.frame, placeholder_text="Type Here...")
        self.entry_ticker.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.input_button = ctk.CTkButton(master=self.frame, text="Input", border_width=2, command=self.printInput)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")

        self.print_ticker = ctk.CTkLabel(master=self.frame, text="")
        self.print_ticker.grid(column=1, row=2)

        self.conclusion_button = ctk.CTkButton(master=self.frame, text="Print Data", border_width=2, command=self.getData)
        self.conclusion_button.grid(column=1, row=3)

        self.print_conclusion = ctk.CTkLabel(master=self.frame, text="")
        self.print_conclusion.grid(column=1, row=4)

        self.type_label = ctk.CTkLabel(master=self.frame, text="Close/Open/High/Low:")
        self.type_label.grid(column=1, row=5)

        self.plot_type = ctk.CTkEntry(master=self.frame)
        self.plot_type.grid(column=1, row=6, sticky="we")

        self.plot_button = ctk.CTkButton(master=self.frame, text="Plot History", border_width=2, command=self.plotHistory)
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
        canvas = FigureCanvasTkAgg(graph, master=self.frame2)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar_frame = tk.Frame(master = self.frame2)
        toolbar_frame.grid(row=1, column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()


class MainApp(ctk.CTk):

    WIDTH=750
    HEIGHT=520

    def __init__(self):
        super(). __init__()

        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("StockAppIA")

        # 2x1 main grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.frame_left = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nswe")

        self.frame_right = ctk.CTkFrame(master=self, corner_radius=21)
        self.frame_right.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")

        #1x2 right grid
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=1)


        self.frame_right_up = ctk.CTkFrame(master=self.frame_right, corner_radius=21)
        self.frame_right_up.grid(row=0, column=0, padx=5, pady=5, sticky="we")

        self.frame_right_down = ctk.CTkFrame(master=self.frame_right, corner_radius=21)
        self.frame_right_down.grid(row=1, column=0, padx=5, pady=5, sticky="we")

        self.initUI()

    def initUI(self):
        # self.statusbar = Statusbar(self.parent)
        # self.navbar = Navbar(self.parent)
        self.toolbar = Toolbar(self.frame_left)
        self.main = MainWindow(self.frame_right_up, self.frame_right_down)
    
    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()