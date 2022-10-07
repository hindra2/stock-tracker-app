import tkinter as tk
import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

ui_path = "/home/harold/Documents/Coding/Compsci IA/compsci-ia/assets/icons/"

ctk.set_appearance_mode("Dark")
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
        self.settings = tk.PhotoImage(file=f"{ui_path}settings.png")
    
    def initUI(self):
        self.home_button = ctk.CTkButton(master=self.frame, 
                                        text="", 
                                        image=self.home, 
                                        fg_color=("white", "grey"),  
                                        width=60, 
                                        corner_radius=6,
                                        command=self.doNothing)
        self.home_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.globe_button = ctk.CTkButton(master=self.frame, 
                                        text="", 
                                        image=self.globe, 
                                        fg_color=("white", "grey"), 
                                        width=60, 
                                        corner_radius=6,
                                        command=self.doNothing)
        self.globe_button.grid(row=1, column=0, padx=5, pady=5)

        self.settings_button = ctk.CTkButton(master=self.frame, 
                                        text="", 
                                        image=self.settings, 
                                        fg_color=("white", "grey"), 
                                        width=60, 
                                        corner_radius=6,
                                        command=self.doNothing)
        self.settings_button.grid(row=2, column=0, padx=5, pady=5)
        
    def doNothing(self):
        print("ASD")



class MainWindow(ctk.CTk):
    def __init__(self, frame):
        self.frame = frame
 
        #1x2 right grid
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1), weight=1)


        self.frame_right_up = ctk.CTkFrame(master=self.frame, corner_radius=21)
        self.frame_right_up.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_up.columnconfigure(1, weight=1)

        self.frame_right_down = ctk.CTkFrame(master=self.frame, corner_radius=21)
        self.frame_right_down.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_down.columnconfigure(0, weight=1)
        self.frame_right_down.rowconfigure(0, weight=1)

        self.initUI()

    def initUI(self):
        self.ticker_label = ctk.CTkLabel(master=self.frame_right_up, 
                                        text="Ticker:", 
                                        corner_radius=21, 
                                        justify=tk.CENTER)
        self.ticker_label.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.entry_ticker = ctk.CTkEntry(master=self.frame_right_up, 
                                        placeholder_text="Type Here...")
        self.entry_ticker.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.input_button = ctk.CTkButton(master=self.frame_right_up,  
                                        text="Input", 
                                        border_width=2, 
                                        command=self.printInput)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")

        self.print_ticker = ctk.CTkLabel(master=self.frame_right_up, text="")
        self.print_ticker.grid(column=1, row=2)

        self.conclusion_button = ctk.CTkButton(master=self.frame_right_up, text="Print Data", border_width=2, command=self.getData)
        self.conclusion_button.grid(column=1, row=3)

        self.print_conclusion = ctk.CTkLabel(master=self.frame_right_up, 
                                            text="Plot Type:",
                                            justify=tk.CENTER)
        self.print_conclusion.grid(column=1, row=4, sticky="we")

        self.type_label = ctk.CTkLabel(master=self.frame_right_up, text="")
        self.type_label.grid(column=0, row=5)

        self.plot_type = ctk.CTkOptionMenu(master=self.frame_right_up, values=["Close", "Open", "High", "Low"])
        self.plot_type.grid(column=1, row=5)

        self.plot_button = ctk.CTkButton(master=self.frame_right_up, text="Plot History", border_width=2, command=self.plotHistory)
        self.plot_button.grid(column=1, row=6)

    def printInput(self):
        self.input_ticker = self.entry_ticker.get()
        self.print_ticker.config(text=f"Ticker: {self.input_ticker}")
        self.stock = Stock(self.input_ticker)

    def getData(self):
        openingPrice = self.stock.getOpeningPrice()
        priceRange = self.stock.getPriceRange()
        volume = self.stock.getVolume()
        name = self.stock.name
        self.print_conclusion.config(text=f"Company Name: {name}\nOpening Price:  {openingPrice}\nPrice Range: {priceRange}\nVolume: {volume}")

    def plotHistory(self):
        type = self.plot_type.get()
        graph = self.stock.plotHistory(type)
        canvas = FigureCanvasTkAgg(graph, master=self.frame_right_down)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar_frame = tk.Frame(master = self.frame_right_down)
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
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        # 2x1 main grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0,1), weight=1)

        self.frame_left = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nswe")

        self.frame_right = ctk.CTkFrame(master=self, corner_radius=6)
        self.frame_right.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")

        self.initUI()

    def initUI(self):
        # self.statusbar = Statusbar(self.parent)
        # self.navbar = Navbar(self.parent)
        self.toolbar = Toolbar(self.frame_left)
        self.main = MainWindow(self.frame_right)
    
    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
