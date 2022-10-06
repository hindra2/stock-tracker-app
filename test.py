import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Window(ctk.CTk):
    def __init__(self, frame):
        super(). __init__()
        self.frame = frame
        self.initUI()

    def initUI(self):
        self.combobox_1 = ctk.CTkComboBox(master=self.frame, values=["Close", "Open", "High", "Low"])
        self.combobox_1.pack()

        self.button = ctk.CTkButton(master=self.frame, text="CLICK TO GET", command=self.getComboBoxValue)
        self.button.pack()

    def getComboBoxValue(self):
        print(self.combobox_1.get())


class Main(ctk.CTk):
    def __init__(self):
        super(). __init__()

        self.initUI()

    def initUI(self):
        self.mainWindow = Window(self)


if __name__ == "__main__":
    app = Main()
    app.mainloop()