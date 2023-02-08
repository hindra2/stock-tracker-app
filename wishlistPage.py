import customtkinter as ctk
from stock import InputStock

class wishlistPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Creates a 1x1 grid
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)

        self.stock_frame = ctk.CTkFrame(self, corner_radius=21)
        self.stock_frame.grid(row=0, column=0, sticky="nswe")

        self.display_frame = ctk.CTkScrollableFrame(self, corner_radius=21, label_anchor="center")
        self.display_frame.grid(row=0, column=1, sticky="nswe")
        self.display_frame.columnconfigure(0, weight=1)

        self.heading  = ctk.CTkLabel(self.stock_frame, text="Tracking Stocks:")
        self.heading.grid(row=1, column=1, sticky="nswe")

        self.button = ctk.CTkButton(self.stock_frame, text="printinfo", command=self.load_data)
        self.button.grid(row=2, column=1, sticky="nswe")


    
    def load_data(self):
        row = 0
        data = InputStock.load_data()
        for dictionary in data:
            for ticker in dictionary:
                content = dictionary[ticker]
                self.card = ctk.CTkFrame(self.display_frame, corner_radius=21)
                self.card.grid(row=row, padx=5, pady=5, sticky="we")
                # self.card.rowconfigure((0,1), weight=1)
                # self.card.columnconfigure((0, 1, 2), weight=1)

                self.ticker_label = ctk.CTkLabel(self.card, text=ticker, font=("Arial", 15))
                self.ticker_label.grid(row=0, column=0, padx=5, pady=5, sticky="we")

                self.count_label = ctk.CTkLabel(self.card, text=content["Count"], font=("Arial", 15))
                self.count_label.grid(row=1, column=0, padx=5, pady=5, sticky="we")

                self.boughtprice_label = ctk.CTkLabel(self.card, text=content["Bought Price"], font=("Arial", 15))
                self.boughtprice_label.grid(row=0, column=1, padx=5, pady=5, sticky="we")

                self.upperbound_label = ctk.CTkLabel(self.card, text=content["Upper Bound"], font=("Arial", 15))
                self.upperbound_label.grid(row=0, column=2, padx=5, pady=5, sticky="we")

                self.lowerbound_label = ctk.CTkLabel(self.card, text=content["Lower Bound"], font=("Arial", 15))
                self.lowerbound_label.grid(row=1, column=2, padx=5, pady=5, sticky="we")

            row += 1

    def onlift(self):
        self.lift()