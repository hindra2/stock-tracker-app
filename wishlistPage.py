import customtkinter as ctk
import pickle
from stock import InputStock

class wishlistPage(ctk.CTkFrame):
    def __init__(self, master, stock_updated):
        super().__init__(master)
        self.stock_updated = stock_updated

        # Creates a 1x1 grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)

        self.heading = ctk.CTkLabel(self, text="Tracking Stocks:", font=("Arial", 25))
        self.heading.grid(row=0, column=0, sticky="we")

        self.load_data()
        self.update_stock()


    def update_stock(self):
        self.stock_updated.wait()
        self.display_frame.destroy()
        self.load_data()
        self.after(10000, self.update_stock)


    def load_data(self):
        self.display_frame = ctk.CTkScrollableFrame(self, corner_radius=21, label_anchor="center")
        self.display_frame.grid(row=1, column=0, sticky="nswe")
        self.display_frame.columnconfigure(0, weight=1)

        row = 0
        data = InputStock.load_data()

        for dictionary in data:
            for ticker in dictionary:
                content = dictionary[ticker]

                if content['Gain'] > 0:
                    color = "#70da36"
                else:
                    color = "#ed4c36"

                self.card = ctk.CTkFrame(self.display_frame, corner_radius=21)
                self.card.grid(row=row, padx=5, pady=5, sticky="we")
                self.card.rowconfigure((0,1), weight=1)
                self.card.columnconfigure((0, 1, 2, 3), weight=1)

                self.ticker_label = ctk.CTkLabel(self.card, text=ticker, font=("Arial", 15))
                self.ticker_label.grid(row=0, column=0, padx=5, pady=5, sticky="we", rowspan=2)

                self.count_label = ctk.CTkLabel(self.card, text="Stock Count", font=("Arial", 15))
                self.count_label.grid(row=0, column=1, padx=5, pady=5, sticky="we")

                self.count = ctk.CTkLabel(self.card, text=content["Count"], font=("Arial", 15))
                self.count.grid(row=1, column=1, padx=5, pady=5, sticky="we")

                self.bought_price_label = ctk.CTkLabel(self.card, text="Bought at", font=("Arial", 15))
                self.bought_price_label.grid(row=0, column=2, padx=5, pady=5, sticky="we")

                self.boughtprice = ctk.CTkLabel(self.card, text=f"${content['Bought Price']}", font=("Arial", 15))
                self.boughtprice.grid(row=1, column=2, padx=5, pady=5, sticky="we")

                self.gain_label = ctk.CTkLabel(self.card, text="Gain", font=("Arial", 15))
                self.gain_label.grid(row=0, column=3, padx=5, pady=5, sticky="we")

                self.gain_label = ctk.CTkLabel(self.card, text=f"{content['Gain']}%", font=("Arial", 15), text_color=color)
                self.gain_label.grid(row=1, column=3, padx=5, pady=5, sticky="we")
            row += 1

    def onlift(self):
        self.lift()