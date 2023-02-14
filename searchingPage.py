# Library Imports
import customtkinter as ctk
from stock import Stock, InputStock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import os
from PIL import Image

# Specifies asset path relative to os
ui_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/icons")

# Searching page class
class SearchingPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # 1x2 right grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)

        # configuring top grid
        self.frame_right_up = ctk.CTkFrame(master=self, corner_radius=21)
        self.frame_right_up.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_up.columnconfigure(1, weight=1)

        # Configuring bottom grid
        self.frame_right_down = ctk.CTkFrame(master=self, corner_radius=21)
        self.frame_right_down.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_down.columnconfigure(0, weight=1)
        self.frame_right_down.rowconfigure(0, weight=1)

        # UI components
        self.ticker_label = ctk.CTkLabel(
                            master=self.frame_right_up,
                            text="Ticker:",
                            corner_radius=21,
                            font=("Arial", 15))
        self.ticker_label.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.entry_ticker = ctk.CTkEntry(
                            master=self.frame_right_up,
                            placeholder_text="Type Here...",
                            font=("Arial", 15))
        self.entry_ticker.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.input_button = ctk.CTkButton(
                            master=self.frame_right_up,
                            text="Input",
                            font=("Arial", 15),
                            command=self.print_input)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")


        self.print_conclusion = ctk.CTkLabel(
                                master=self.frame_right_up,
                                text="",
                                font=("Arial", 15))
        self.print_conclusion.grid(column=1, row=3, sticky="we", padx=10, pady=10)

        self.type_label = ctk.CTkLabel(
                        master=self.frame_right_up,
                        text="Plot Type:",
                        font=("Arial", 15))
        self.type_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

        self.type = "Close/Open"
        self.plot_type = ctk.CTkSegmentedButton(
                        master=self.frame_right_up,
                        values=["Close/Open", "High/Low"],
                        font=("Arial", 15),
                        command=self.set_type)
        self.plot_type.grid(column=1, row=4, padx=10, pady=10)
        self.plot_type.set("Close/Open")

        self.period_label = ctk.CTkLabel(
                            master=self.frame_right_up,
                            text="Time Period:",
                            font=("Arial", 15))
        self.period_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")

        # self.period = ctk.StringVar(value="1d")
        self.period = "1d"
        self.plot_period = ctk.CTkSegmentedButton(
                        master=self.frame_right_up,
                        values=["1d", "5d", "1mo", "6mo", "1y", "5y", "ytd"],
                        font=("Arial", 15),
                        command=self.set_period)
        self.plot_period.grid(column=1, row=5, padx=10, pady=10)
        self.plot_period.set("1d")

        self.graph_button = ctk.CTkButton(
                            master=self.frame_right_up,
                            text="Generate Graph",
                            font=("Arial", 15),
                            command=self.plot_history)
        self.graph_button.grid(column=1, row=6, padx=10, pady=10)

        self.add = ctk.CTkImage(Image.open(os.path.join(ui_path, "plus.png")), size=(35, 35))
        self.add_button = ctk.CTkButton(
                        master=self.frame_right_down,
                        text="",
                        image=self.add,
                        fg_color="transparent",
                        width=60,
                        hover_color=("gray70", "gray30"),
                        command=self.display_input_window)
        self.add_button.grid(row=4, column=2, padx=5, pady=5, sticky="s")

    # Funciton that creates a TopLevel window for the user to input information that they want to track
    def display_input_window(self):
        self.input_window = ctk.CTkToplevel(self)
        self.input_window.geometry("500x400")
        self.input_window.title("Input Bought Stock:")
        self.input_window.columnconfigure((0, 1), weight=1)

        count_label = ctk.CTkLabel(master=self.input_window, text="Count:")
        count_label.grid(column=0, row=0, sticky="e", pady=20)

        self.count_entry = ctk.CTkEntry(master=self.input_window, font=("Arial", 15))
        self.count_entry.grid(column=1, row=0, sticky="we", pady=20, padx=50)


        bought_label = ctk.CTkLabel(master=self.input_window, text="Bought Price:")
        bought_label.grid(column=0, row=1, sticky="e", pady=20)

        self.bought_entry = ctk.CTkEntry(master=self.input_window, font=("Arial", 15))
        self.bought_entry.grid(column=1, row=1, sticky="we", pady=20, padx=50)

        submit_button = ctk.CTkButton(
                        master=self.input_window,
                        text="Submit",
                        corner_radius=21,
                        font=("Arial", 15),
                        command=self.input_data)
        submit_button.grid(column=0, row=4, columnspan=2, padx=50, pady=20, sticky="we")

    def input_data(self):
        try:
            ticker = self.entry_ticker.get()
            count = self.count_entry.get()
            bought_price = self.bought_entry.get()

            self.userstock = InputStock(ticker, count, bought_price)
            self.userstock.dump_data()

            self.input_window.destroy()
        except TypeError:
            print("No Ticker Specified")

    # Function that creates an instance of the Stock class and prints the info on the label print_conclusion
    def print_input(self):
        ticker = self.entry_ticker.get()
        self.stock = Stock(ticker)
        opening_price = self.stock.getOpeningPrice()
        price_range = self.stock.getPriceRange()
        volume = self.stock.getVolume()
        name = self.stock.getName()
        self.print_conclusion.configure(text=f"Company Name: {name}\nOpening Price:  ${opening_price}\nPrice Range: ${price_range}\nVolume: {volume}")

    def set_period(self, period):
        self.period = period
    
    def set_type(self, _type):
        self.type = _type

    # Function that calls plotHistory from the instance of the Stock class in the variabke self.stock
    def plot_history(self):
        try:
            # Stores the graph from plotHistory into a variable and places the graph on a canvas
            if self.type == "Close/Open":
                graph = self.stock.plotHistory("Close", "Open", self.period)
            else:
                graph = self.stock.plotHistory("High", "Low", self.period)
            canvas = FigureCanvasTkAgg(graph, master=self.frame_right_down)
            canvas.get_tk_widget().grid(row=0, column=0)
            # Implements the matplotlib toolbar below the graph
            toolbar_frame = ctk.CTkFrame(master=self.frame_right_down)
            toolbar_frame.grid(row=1, column=0)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()
            
        # Error handling for when user doesn't type a ticker in the search bar
        except AttributeError as e:
            print(f"Error: {e}")

    # Function to implement window switching
    def onlift(self):
        self.lift()