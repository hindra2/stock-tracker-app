# Library Imports
import customtkinter as ctk
from PIL import Image
import os
import webbrowser

# Specify image path relative to os
ui_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/learning")

# Learning page class
class learningPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Images
        self.investopedia = ctk.CTkImage(Image.open(os.path.join(ui_path, "investopedia.png")), size=(233,44))
        self.youtube = ctk.CTkImage(Image.open(os.path.join(ui_path, "youtube.png")), size=(233,44))

        # Frames
        self.content_frame = ctk.CTkFrame(master=self, corner_radius=21)
        self.content_frame.grid(row=0, column=0, sticky="nswe")

        self.text_tutorials = ctk.CTkFrame(master=self.content_frame, corner_radius=21, fg_color="#404040")
        self.text_tutorials.grid(row=0, column=0, sticky="nswe", pady=30, padx=30)

        self.video_tutorials = ctk.CTkFrame(master=self.content_frame, corner_radius=21, fg_color="#404040")
        self.video_tutorials.grid(row=0, column=1, sticky="nswe", pady=30, padx=30)

        # Links and UI components of Investopedia learning resources
        self.investopedia_label = ctk.CTkLabel(self.text_tutorials,
                                                image=self.investopedia,
                                                text="",
                                                fg_color="transparent")
        self.investopedia_label.grid(row=0, column=0, sticky="nswe", pady=30, padx=50)

        self.investing_investopedia_button = ctk.CTkButton(self.text_tutorials,
                                                text="Investing Essentials",
                                                fg_color="transparent",
                                                font=("Arial", 30),
                                                width=120,
                                                height=30,
                                                command=lambda: self.web("https://www.investopedia.com/investing-essentials-4689754"))
        self.investing_investopedia_button.grid(row=1, column=0, pady=30, padx=30)

        self.portflio_investopedia_button = ctk.CTkButton(self.text_tutorials,
                                                text="Portfolio Management", 
                                                font=("Arial", 30),
                                                fg_color="transparent",
                                                width=120,
                                                height=30,
                                                command=lambda: self.web("https://www.investopedia.com/portfolio-management-4689745"))
        self.portflio_investopedia_button.grid(row=2, column=0, pady=0, padx=30)

        # Links and UI Components of Adam Khoo Youtube Channel
        self.youtube_label = ctk.CTkLabel(self.video_tutorials,
                                                image=self.youtube,
                                                text="",
                                                fg_color="transparent")
        self.youtube_label.grid(row=0, column=0, sticky="nswe", pady=30, padx=50)

        self.adam_khoo_button = ctk.CTkButton(self.video_tutorials,
                                                text="Adam Khoo", 
                                                font=("Arial", 30),
                                                fg_color="transparent",
                                                width=120,
                                                height=30,
                                                command=lambda: self.web("https://www.youtube.com/@AdamKhoo"))
        self.adam_khoo_button.grid(row=1, column=0, pady=30, padx=30)

    # Function to open links
    def web(self, url):
        webbrowser.open_new(url)

    # Function to implement window switching
    def onlift(self):
        self.lift()