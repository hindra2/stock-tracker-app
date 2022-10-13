import tkinter as tk
import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


# Global Variables
ui_path = "./assets/icons/"

# Initial seettings
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")


class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuring Grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        # UI Elements For Login Page
        self.username_label = ctk.CTkLabel(master=self, text="Username:")
        self.username_label.grid(column=0, row=0, padx=50, pady=25)

        self.user_username = ctk.CTkEntry(master=self)
        self.user_username.grid(column=1, row=0, padx=50, pady=25, sticky="nswe")

        self.password_label = ctk.CTkLabel(master=self, text="Password:")
        self.password_label.grid(column=0, row=1, padx=50, pady=25)

        self.user_password = ctk.CTkEntry(master=self)
        self.user_password.grid(column=1, row=1, padx=50, pady=25, sticky="nswe")

        self.login_button = ctk.CTkButton(master=self,
                                          text="Login",
                                          command=lambda: self.callback())
        self.login_button.grid(column=0, row=2, columnspan=2, padx=50, pady=25, sticky="nswe")

    def onlift(self):
        self.lift()


class MainWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()
        # 1x2 right grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)

        # configuring top grid
        self.frame_right_up = ctk.CTkFrame(master=self, corner_radius=21)
        self.frame_right_up.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_up.columnconfigure(1, weight=1)

        # Configuring bottom grid
        self.frame_right_down = ctk.CTkFrame(master=self, corner_radius=21)
        self.frame_right_down.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.frame_right_down.columnconfigure(0, weight=1)
        self.frame_right_down.rowconfigure(0, weight=1)

        self.initUI()

    def initUI(self):
        self.ticker_label = ctk.CTkLabel(master=self.frame_right_up,
                                         text="Ticker:",
                                         corner_radius=21,
                                         text_font=("Arial", 15))
        self.ticker_label.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.entry_ticker = ctk.CTkEntry(master=self.frame_right_up,
                                         placeholder_text="Type Here...",
                                         text_font=("Arial", 15))
        self.entry_ticker.grid(column=1, row=1, padx=10, pady=10, sticky="we")

        self.input_button = ctk.CTkButton(master=self.frame_right_up,
                                          text="Input",
                                          text_font=("Arial", 15),
                                          command=self.printInput)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")

        self.print_ticker = ctk.CTkLabel(master=self.frame_right_up,
                                         text="",
                                         text_font=("Arial", 15))
        self.print_ticker.grid(column=1, row=2, padx=10, pady=10)

        self.conclusion_button = ctk.CTkButton(master=self.frame_right_up,
                                               text="Scrape Data",
                                               text_font=("Arial", 15),
                                               command=self.getData)
        self.conclusion_button.grid(column=1, row=3, padx=10, pady=10)

        self.print_conclusion = ctk.CTkLabel(master=self.frame_right_up,
                                             text="",
                                             text_font=("Arial", 15))
        self.print_conclusion.grid(column=1, row=4, sticky="we", padx=10, pady=10)

        self.type_label = ctk.CTkLabel(master=self.frame_right_up,
                                       text="Plot Type:",
                                       text_font=("Arial", 15))
        self.type_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")

        self.plot_type = ctk.CTkOptionMenu(master=self.frame_right_up,
                                           values=["Close", "Open", "High", "Low"],
                                           text_font=("Arial", 15),
                                           command=self.plotHistory)
        self.plot_type.grid(column=1, row=5, padx=10, pady=10)

    def printInput(self):
        ticker = self.entry_ticker.get()
        self.print_ticker.configure(text=f"Ticker: {ticker}")
        self.stock = Stock(ticker)

    def getData(self):
        openingPrice = self.stock.getOpeningPrice()
        priceRange = self.stock.getPriceRange()
        volume = self.stock.getVolume()
        name = self.stock.name
        self.print_conclusion.configure(text=f"Company Name: {name}\nOpening Price:  {openingPrice}\nPrice Range: {priceRange}\nVolume: {volume}")

    def plotHistory(self, type):
        graph = self.stock.plotHistory(type)
        canvas = FigureCanvasTkAgg(graph, master=self.frame_right_down)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar_frame = tk.Frame(master=self.frame_right_down)
        toolbar_frame.grid(row=1, column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

    def onlift(self):
        self.lift()


class MainApp(ctk.CTk):
    WIDTH = 750
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("StockAppIA")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        # 2x1 main grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0,1), weight=1)

        self.frame_left = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.frame_left.rowconfigure(1, weight=1)

        # Constant Window Components
        self.initImage()
        self.initSettingsUI()

        # Changing Window Components
        self.page1 = LoginPage(self)
        self.page1.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.page2 = MainWindow(self)
        self.page2.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")

        self.page1.callback = self.page2.onlift

        self.page1.lift()

    # Images for Toolbar Buttons
    def initImage(self):
        self.home = tk.PhotoImage(file=f"{ui_path}home.png")
        self.globe = tk.PhotoImage(file=f"{ui_path}globe.png")
        self.settings = tk.PhotoImage(file=f"{ui_path}settings.png")

    # Toolbar UI
    def initSettingsUI(self):
        self.home_button = ctk.CTkButton(master=self.frame_left,
                                         text="",
                                         image=self.home,
                                         fg_color="white",
                                         width=60,
                                         corner_radius=6,
                                         command=self.lift)
        self.home_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.globe_button = ctk.CTkButton(master=self.frame_left,
                                          text="",
                                          image=self.globe,
                                          fg_color="white",
                                          width=60,
                                          corner_radius=6,
                                          command="")
        self.globe_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        self.settings_button = ctk.CTkButton(master=self.frame_left,
                                             text="",
                                             image=self.settings,
                                             fg_color="white",
                                             width=60,
                                             corner_radius=6,
                                             command=self.displaySettingsWindow)
        self.settings_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    def displaySettingsWindow(self):
        settings_window = ctk.CTkToplevel(self.frame_left)
        settings_window.geometry("500x400")
        settings_window.title("Settings")
        settings_window.columnconfigure((0, 1), weight=1)

        appearance_label = ctk.CTkLabel(master=settings_window, text="Appearance:")
        appearance_label.grid(column=0, row=0, sticky="e", pady=20)

        appearance_option_menu = ctk.CTkOptionMenu(master=settings_window,
                                                   values=["Dark", "Light"],
                                                   command=self.change_appearance_mode)
        appearance_option_menu.grid(column=1, row=0, sticky="w", pady=20)

        # Settings Functions
    def change_appearance_mode(self, new_appearance_mode):
            ctk.set_appearance_mode(new_appearance_mode)

    def onClosing(self, event=0):
        self.quit()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
