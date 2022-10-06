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
        self.label = ctk.CTkLabel(master=self.frame, text="Hello World", fg_color=("white", "gray38"), corner_radius=6)
        self.label.grid(row=0, column=0)


class Main(ctk.CTk):
    def __init__(self):
        super(). __init__()

        self.initUI()

    def initUI(self):
        self.mainWindow = Window(self)


if __name__ == "__main__":
    app = Main()
    app.mainloop()