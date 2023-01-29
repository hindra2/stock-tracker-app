import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import os
from PIL import Image

ui_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/icons")

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

        # Initializing the UI
        self.ticker_label = ctk.CTkLabel(master=self.frame_right_up,
                                         text="Ticker:",
                                         corner_radius=21,
                                         font=("Arial", 15))
        self.ticker_label.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.entry_ticker = ctk.CTkEntry(master=self.frame_right_up,
                                         placeholder_text="Type Here...",
                                         font=("Arial", 15))
        self.entry_ticker.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.input_button = ctk.CTkButton(master=self.frame_right_up,
                                          text="Input",
                                          font=("Arial", 15),
                                          command=self.print_input)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")

        # self.print_ticker = ctk.CTkLabel(master=self.frame_right_up,
        #                                  text="",
        #                                  font=("Arial", 15))
        # self.print_ticker.grid(column=1, row=2, padx=10, pady=10)

        self.print_conclusion = ctk.CTkLabel(master=self.frame_right_up,
                                             text="",
                                             font=("Arial", 15))
        self.print_conclusion.grid(column=1, row=3, sticky="we", padx=10, pady=10)

        self.type_label = ctk.CTkLabel(master=self.frame_right_up,
                                       text="Plot Type:",
                                       font=("Arial", 15))
        self.type_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

        self.plot_type = ctk.CTkOptionMenu(master=self.frame_right_up,
                                           values=["Close", "Open", "High", "Low"],
                                           font=("Arial", 15),
                                           command=self.plot_history)
        self.plot_type.grid(column=1, row=4, padx=10, pady=10)

        self.add = ctk.CTkImage(Image.open(os.path.join(ui_path, "plus.png")), size=(35, 35))
        self.add_button = ctk.CTkButton(master=self.frame_right_down,
                                             text="",
                                             image=self.add,
                                             fg_color="transparent",
                                             width=60,
                                             hover_color=("gray70", "gray30"),
                                             command=self.display_input_window)
        self.add_button.grid(row=4, column=2, padx=5, pady=5, sticky="s")

    def display_input_window(self):
        input_window = ctk.CTkToplevel(self)
        input_window.geometry("500x400")
        input_window.title("Input Bought Stock:")
        input_window.columnconfigure((0, 1), weight=1)

        count_label = ctk.CTkLabel(master=input_window, text="Count:")
        count_label.grid(column=0, row=0, sticky="e", pady=20)

        count_entry = ctk.CTkEntry(master=input_window, font=("Arial", 15))
        count_entry.grid(column=1, row=0, sticky="we", pady=20, padx=50)


        bought_label = ctk.CTkLabel(master=input_window, text="Bought Price:")
        bought_label.grid(column=0, row=1, sticky="e", pady=20)

        bought_entry = ctk.CTkEntry(master=input_window, font=("Arial", 15))
        bought_entry.grid(column=1, row=1, sticky="we", pady=20, padx=50)


        upper_bound_label = ctk.CTkLabel(master=input_window, text="Upper Bound:")
        upper_bound_label.grid(column=0, row=2, sticky="e", pady=20)

        upper_bound_entry= ctk.CTkEntry(master=input_window, font=("Arial", 15))
        upper_bound_entry.grid(column=1, row=2, sticky="we", pady=20, padx=50)


        lower_bound_label = ctk.CTkLabel(master=input_window, text="Lower Bound:")
        lower_bound_label.grid(column=0, row=3, sticky="e", pady=20)

        lower_bound_entry = ctk.CTkEntry(master=input_window, font=("Arial", 15))
        lower_bound_entry.grid(column=1, row=3, sticky="we", pady=20, padx=50)

        submit_button = ctk.CTkButton(master=input_window,
                                    text="Submit",
                                    corner_radius=21,
                                    font=("Arial", 15))
        submit_button.grid(column=0, row=4, columnspan=2, padx=50, pady=20, sticky="we")

    def print_input(self):
        ticker = self.entry_ticker.get()
        # self.print_ticker.configure(text=f"Ticker: {ticker}")
        self.stock = Stock(ticker)
        opening_price = self.stock.getOpeningPrice(ticker)
        price_range = self.stock.getPriceRange()
        volume = self.stock.getVolume()
        name = self.stock.getName()
        self.print_conclusion.configure(text=f"Company Name: {name}\nOpening Price:  ${opening_price}\nPrice Range: ${price_range}\nVolume: {volume}")

    def plot_history(self, type):
        graph = self.stock.plotHistory(type)
        canvas = FigureCanvasTkAgg(graph, master=self.frame_right_down)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar_frame = ctk.CTkFrame(master=self.frame_right_down)
        toolbar_frame.grid(row=1, column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

    def onlift(self):
        self.lift()