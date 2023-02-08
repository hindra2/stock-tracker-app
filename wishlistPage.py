import customtkinter as ctk
from stock import InputStock

class wishlistPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Creates a 1x1 grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.stock_frame = ctk.CTkFrame(self, corner_radius=21)
        self.stock_frame.grid(row=1, column=1, sticky="nswe")

        self.heading  = ctk.CTkLabel(self.stock_frame, text="Tracking Stocks:")
        self.heading.grid(row=1, column=1, sticky="nswe")

        self.button = ctk.CTkButton(self.stock_frame, text="printinfo", command=self.load_data)
        self.button.grid(row=2, column=1, sticky="nswe")
    
    def load_data(self):
        print(InputStock.load_data())
        data = InputStock.load_data()
        for i in data:
            print(i)
        # [{'MSFT': {'Count': '100', 'Bought Price': '123', 'Upper Bound': '123', 'Lower Bound': '123'}}, {'TSLA': {'Count': '123123', 'Bought Price': '333', 'Upper Bound': '3', 'Lower Bound': '22'}}]

    def onlift(self):
        self.lift()