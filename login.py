import tkinter
import customtkinter as ctk
import pandas as pd


class Login:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

        self.information = None # open csv

    def saveLoginInfo(self):
        # write login info in txt file
        pass


class MainApp(ctk.CTk):

    WIDTH=480
    HEIGHT=300

    def __init__(self):
        super(). __init__()

        self.geometry(f"{MainApp.WIDTH}x{MainApp.HEIGHT}")
        self.title("Login")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.initUI()


    def onClosing(self, event=0):
        self.quit()

    def initUI(self):
        self.center_frame = ctk.CTkFrame(master=self, corner_radius=6)
        self.center_frame.grid(column=0, row=0, sticky="nswe")

        self.columnconfigure((0), weight=1)
        self.center_frame.columnconfigure((0), weight=1)


        self.username_label = ctk.CTkLabel(master=self.center_frame, text="Username:")
        self.username_label.grid(column=0, row=0, padx=50, pady=25)

        self.user_username = ctk.CTkEntry(master=self.center_frame)
        self.user_username.grid(column=1, row=0, padx=50, pady=25, sticky="nswe")

        self.password_label = ctk.CTkLabel(master=self.center_frame, text="Password:")
        self.password_label.grid(column=0, row=1, padx=50, pady=25)

        self.user_password = ctk.CTkEntry(master=self.center_frame)
        self.user_password.grid(column=1, row=1, padx=50, pady=25, sticky="nswe")

        self.login_button = ctk.CTkButton(master=self.center_frame, text="Login")
        self.login_button.grid(column=0, row=2, columnspan=2, padx=50, pady=25, sticky="nswe")
