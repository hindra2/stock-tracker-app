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

        # Configuring Grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        # UI Elements For Login Page
        self.username_label = ctk.CTkLabel(master=self, text="Username:", text_font=("Arial", 15))
        self.username_label.grid(column=0, row=0, padx=50, pady=25, sticky="we")

        self.user_username = ctk.CTkEntry(master=self, text_font=("Arial", 15))
        self.user_username.grid(column=1, row=0, padx=50, pady=25, sticky="we")

        self.password_label = ctk.CTkLabel(master=self, text="Password:", text_font=("Arial", 15))
        self.password_label.grid(column=0, row=1, padx=50, pady=25, sticky="we")

        self.user_password = ctk.CTkEntry(master=self, text_font=("Arial", 15))
        self.user_password.grid(column=1, row=1, padx=50, pady=25, sticky="we")

        self.login_button = ctk.CTkButton(master=self,
                                          text="Login",
                                          command=lambda: self.callback(),
                                          text_font=("Arial", 15))
        self.login_button.grid(column=0, row=2, columnspan=2, padx=50, pady=50, sticky="nswe")

    def onlift(self):
        self.lift()


class SearchingPage(ctk.CTkFrame):
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

        # Initializing the UI
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
                                          command=self.print_input)
        self.input_button.grid(column=2, row=1, padx=10, pady=10, sticky="we")

        self.print_ticker = ctk.CTkLabel(master=self.frame_right_up,
                                         text="",
                                         text_font=("Arial", 15))
        self.print_ticker.grid(column=1, row=2, padx=10, pady=10)

        self.print_conclusion = ctk.CTkLabel(master=self.frame_right_up,
                                             text="",
                                             text_font=("Arial", 15))
        self.print_conclusion.grid(column=1, row=3, sticky="we", padx=10, pady=10)

        self.type_label = ctk.CTkLabel(master=self.frame_right_up,
                                       text="Plot Type:",
                                       text_font=("Arial", 15))
        self.type_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

        self.plot_type = ctk.CTkOptionMenu(master=self.frame_right_up,
                                           values=["Close", "Open", "High", "Low"],
                                           text_font=("Arial", 15),
                                           command=self.plot_history)
        self.plot_type.grid(column=1, row=4, padx=10, pady=10)

    def print_input(self):
        ticker = self.entry_ticker.get()
        self.print_ticker.configure(text=f"Ticker: {ticker}")
        opening_price = Stock(ticker).getOpeningPrice()
        price_range = Stock(ticker).getPriceRange()
        volume = Stock(ticker).getVolume()
        stock_name = Stock(ticker).name()
        self.print_conclusion.configure(text=f"Company Name: {stock_name}\nOpening Price:  {opening_price}\nPrice Range: {price_range}\nVolume: {volume}")

    def plot_history(self, type):
        graph = self.stock.plotHistory(type)
        canvas = FigureCanvasTkAgg(graph, master=self.frame_right_down)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar_frame = tk.Frame(master=self.frame_right_down)
        toolbar_frame.grid(row=1, column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

    def onlift(self):
        self.lift()


class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self.button = ctk.CTkButton(master=self, text="Hello")
        self.button.grid(row=0, column=0)

    def onlift(self):
        self.lift()


class MainApp(ctk.CTk):
    WIDTH = 750
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("StockAppIA")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 2x1 main grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0, 1), weight=1)

        self.frame_left = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.frame_left.rowconfigure(1, weight=1)

        # Changing Window Components
        self.login_page = LoginPage(self)
        self.login_page.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="nswe")
        self.searching_page = SearchingPage(self)
        self.searching_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.home_page = HomePage(self)
        self.home_page = HomePage(self)
        self.home_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")

        self.login_page.callback = self.home_page.onlift
        self.home_page.callback = self.searching_page.onlift

        self.login_page.lift()

        # Constant Window Components --TOOLBAR--
        # Images for Toolbar Buttons
        self.home = tk.PhotoImage(file=f"{ui_path}home.png")
        self.globe = tk.PhotoImage(file=f"{ui_path}globe.png")
        self.settings = tk.PhotoImage(file=f"{ui_path}settings.png")

        # Toolbar UI
        self.home_button = ctk.CTkButton(master=self.frame_left,
                                         text="",
                                         image=self.home,
                                         fg_color="white",
                                         width=60,
                                         corner_radius=6,
                                         command=self.home_page.onlift)
        self.home_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.globe_button = ctk.CTkButton(master=self.frame_left,
                                          text="",
                                          image=self.globe,
                                          fg_color="white",
                                          width=60,
                                          corner_radius=6,
                                          command=self.searching_page.onlift)
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
                                                   values=["Light", "Dark"],
                                                   command=self.change_appearance_mode)
        appearance_option_menu.grid(column=1, row=0, sticky="w", pady=20)

    # Settings Functions
    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.quit()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
