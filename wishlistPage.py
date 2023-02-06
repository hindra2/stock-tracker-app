import customtkinter as ctk
from stock import InputStock

class wishlistPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkButton(self, text="printinfo", command=self.load_data)
        self.label.grid(row=0, column=0)
    
    def load_data(self):
        print(InputStock.load_data())

    def onlift(self):
        self.lift()