# Library Imports
import customtkinter as ctk
from stock import Stock
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image
import os
from tktooltip import ToolTip

# File IMports
import searchingPage
import homePage
import learningPage
import wishlistPage
import loginPage
import loginPage
import time
import threading

# Specify image path relative to os
ui_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/icons")

# Theme settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Main window class
class MainApp(ctk.CTk):
    # Width and Height of app window
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, news_queue, aqueue, stock_updated,):
        # To inherit properties of CTk parent class
        super().__init__()
        #Multithreading
        self.news_queue = news_queue
        self.stock_updated = stock_updated


        self.asset_dict = aqueue.get()
        self.add = self.asset_dict["add"]

        # General App Settings
        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("StockAppIA")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 2x1 main grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Creates customtkinter frame for the navigation bar
        self.navigation_frame = ctk.CTkFrame(master=self, corner_radius=0, width=70)
        self.navigation_frame.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.navigation_frame.rowconfigure(1, weight=1)

        # Splits the navigation_frame to top and bottom
        self.navigation_frame_top = ctk.CTkFrame(master=self.navigation_frame, corner_radius=0, width=70, fg_color="transparent")
        self.navigation_frame_top.grid(row=0, column=0, pady=10, sticky="nswe")

        self.navigation_frame_bottom = ctk.CTkFrame(master=self.navigation_frame, corner_radius=0, width=70, fg_color="transparent")
        self.navigation_frame_bottom.grid(row=1, column=0, pady=10, sticky="s")

        # Different pages for navigation bar to switch into
        self.learning_page = learningPage.learningPage(self)
        self.learning_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.wishlist_page = wishlistPage.wishlistPage(self, self.stock_updated)
        self.wishlist_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.searching_page = searchingPage.SearchingPage(self, self.add)
        self.searching_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.home_page = homePage.HomePage(self, self.news_queue)
        self.home_page.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.login_page = loginPage.LoginPage(self, self.set_username)

        # Page the app starts with - homePage
        self.home_page.callback = self.searching_page.onlift

        # Toolbar
        # Images for Toolbar Buttons

        # Navigation UI Layouting
        self.home_button = ctk.CTkButton(master=self.navigation_frame_top,
                                         text="",
                                         image=ctk.CTkImage(Image.open(self.asset_dict["home"]), size=(35, 35)),
                                         width=60,
                                         hover_color=("gray70", "gray30"),
                                         fg_color="transparent",
                                         command=self.home_page.onlift)
        self.home_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.globe_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=ctk.CTkImage(Image.open(self.asset_dict["search"]), size=(35, 35)),
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),
                                          command=self.searching_page.onlift)
        self.globe_button.grid(row=1, column=0, padx=5, pady=5, sticky="n")


        self.list_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=ctk.CTkImage(Image.open(self.asset_dict["bookmark"]), size=(35, 35)),
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),
                                          command=self.wishlist_page.onlift)
        self.list_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.learn_button = ctk.CTkButton(master=self.navigation_frame_top,
                                          text="",
                                          image=ctk.CTkImage(Image.open(self.asset_dict["learning"]), size=(35, 35)),
                                          fg_color="transparent",
                                          width=60,
                                          hover_color=("gray70", "gray30"),
                                          command=self.learning_page.onlift)
        self.learn_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.logout_button = ctk.CTkButton(master=self.navigation_frame_bottom,
                                             text="",
                                             image=ctk.CTkImage(Image.open(self.asset_dict["logout"]), size=(35, 35)),
                                             fg_color="transparent",
                                             width=60,
                                             hover_color=("gray70", "gray30"),
                                             command=self.logout_func)
        self.logout_button.grid(row=0, column=0, padx=5, pady=5, sticky="s")

    def set_username(self, user):
        self.username = user
        print(user)
        ToolTip(self.logout_button, msg=f"Logged in as: {self.username}", delay=0, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
        self.update()

    # Handling for closing the app
    def on_closing(self, event=0):
        self.quit()
        
    def logout_func(self):
        self.withdraw()
        self.login_page.deiconify()