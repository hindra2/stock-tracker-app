import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image
import os
import schedule

import loginPage
import searchingPage
import homePage

# Global Variables
ui_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/icons")

# Initial seettings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class MainApp(ctk.CTk):
    WIDTH = 1920
    HEIGHT = 1080

    def __init__(self):
        super().__init__()

        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("StockAppIA")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 2x1 main grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0, 1), weight=1)

        self.navigation_frame = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.navigation_frame.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.navigation_frame.rowconfigure(1, weight=1)

        self.navigation_frame_top = ctk.CTkFrame(master=self.navigation_frame, corner_radius=0, width=70, fg_color="transparent")
        self.navigation_frame_top.grid(row=0, column=0, pady=10, sticky="nswe")
        # self.navigation_frame.rowconfigure(1, weight=1)

        self.navigation_frame_bottom = ctk.CTkFrame(master=self.navigation_frame, corner_radius=0, width=70, fg_color="transparent")
        self.navigation_frame_bottom.grid(row=1, column=0, pady=10, sticky="s")
        # self.navigation_frame_bottom.rowconfigure(1, weight=1)

        # Changing Window Components
        self.searching_page = searchingPage.SearchingPage(self)
        self.searching_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.home_page = homePage.HomePage(self)
        self.home_page = homePage.HomePage(self)
        self.home_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")

        # self.login_page.callback = self.home_page.onlift
        self.home_page.callback = self.searching_page.onlift

        # Constant Window Components --TOOLBAR--
        # Images for Toolbar Buttons
        self.home = ctk.CTkImage(Image.open(os.path.join(ui_path, "home.png")), size=(35, 35))
        self.globe = ctk.CTkImage(Image.open(os.path.join(ui_path, "search.png")), size=(35, 35))
        self.list = ctk.CTkImage(Image.open(os.path.join(ui_path, "bookmark.png")), size=(35, 35))
        self.learn = ctk.CTkImage(Image.open(os.path.join(ui_path, "learning.png")), size=(35, 35))
        self.settings = ctk.CTkImage(Image.open(os.path.join(ui_path, "settings.png")), size=(35, 35))
        # Navigation UI
        self.home_button = ctk.CTkButton(master=self.navigation_frame_top,
                                         text="",
                                         image=self.home,
                                         width=60,
                                         hover_color=("gray70", "gray30"),
                                         fg_color="transparent",
                                         command=self.home_page.onlift)
        self.home_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.globe_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=self.globe,
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),
                                          command=self.searching_page.onlift)
        self.globe_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")


        self.list_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=self.list,
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),)
        self.list_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")


        self.learn_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=self.learn,
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),)
        self.learn_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.settings_button = ctk.CTkButton(master=self.navigation_frame_bottom,
                                             text="",
                                             image=self.settings,
                                             fg_color="transparent",
                                             width=60,
                                             hover_color=("gray70", "gray30"),
                                             command=self.displaySettingsWindow)
        self.settings_button.grid(row=0, column=0, padx=5, pady=5, sticky="s")

    def displaySettingsWindow(self):
        settings_window = ctk.CTkToplevel(self.navigation_frame)
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
