import customtkinter as ctk
import webbrowser
import scraper

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(1, weight=1)

        # Frames
        self.stock_frame_top = ctk.CTkFrame(master=self, corner_radius=21)
        self.stock_frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.stock_frame_top.columnconfigure(0, weight=1)

        self.stock_frame_bottom = ctk.CTkFrame(master=self, corner_radius=15)
        self.stock_frame_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.stock_frame_bottom.columnconfigure(0, weight=1)

        self.news_frame_top = ctk.CTkFrame(master=self, corner_radius=21)
        self.news_frame_top.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.news_frame_top.columnconfigure(0, weight=1)

        self.news_frame_bottom = ctk.CTkFrame(master=self, corner_radius=15)
        self.news_frame_bottom.grid(row=1, column=1, padx=5, pady=5, sticky="nswe")
        self.news_frame_bottom.columnconfigure(0, weight=1)


        # Stock data components
        self.stock_head = ctk.CTkLabel(master=self.stock_frame_top, text="Top Stocks", font=("Arial", 25))
        self.stock_head.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # News components
        self.news_head = ctk.CTkLabel(master=self.news_frame_top, text="Headlines", font=("Arial", 25))
        self.news_head.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        headlines = scraper.scrape()
        for i in headlines:
            self.news_label = ctk.CTkButton(self.news_frame_bottom, 
                                            text=headlines[i][0], 
                                            fg_color="gray23",  
                                            hover_color=("gray70", "gray30"), 
                                            font=("Arial", 30),
                                            command=lambda: self.web(headlines[i][1]))
            self.news_label.grid(row=i, pady=6, padx=30, sticky="we")
    
    def web(self, url):
        webbrowser.open_new(url)
    
    def onlift(self):
        self.lift()