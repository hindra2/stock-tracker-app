# Library Imports
import customtkinter as ctk
import webbrowser
import scraper

# Home Page main class
class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        # Inherits properties of CTkFrame, and passes in master as the root of the Frame
        super().__init__(master)

        # Sets a 2x1 grid
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
        self.news_frame_bottom.rowconfigure(0, weight=1)


        # Stock data components
        self.stock_head = ctk.CTkLabel(master=self.stock_frame_top, text="Top Stocks", font=("Arial", 25))
        self.stock_head.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # News components
        self.news_head = ctk.CTkLabel(master=self.news_frame_top, text="Headlines", font=("Arial", 25))
        self.news_head.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.news_tab = ctk.CTkTabview(master=self.news_frame_bottom, corner_radius=21)
        self.news_tab.grid(row=0, sticky="nswe", padx=5)

        # Different tabs for different news sources
        self.bbc_tab = self.news_tab.add("BBC")
        self.bbc_tab.columnconfigure(0, weight=1)
        self.bbc_tab.rowconfigure(0, weight=1)

        self.bbc_scroll_frame = ctk.CTkScrollableFrame(self.bbc_tab, corner_radius=21)
        self.bbc_scroll_frame.grid(row=0, column=0, sticky="nswe")
        self.bbc_scroll_frame.columnconfigure(0, weight=1)

        self.display_bbc_headlines()

        self.yfinance_tab = self.news_tab.add("Yahoo Finance")
        self.yfinance_tab.columnconfigure(0, weight=1)
        self.yfinance_tab.rowconfigure(0, weight=1)

        self.yfinance_scroll_frame = ctk.CTkScrollableFrame(self.yfinance_tab, corner_radius=21)
        self.yfinance_scroll_frame.grid(row=0, column=0, sticky="nswe")
        self.yfinance_scroll_frame.columnconfigure(0, weight=1)

        self.display_yfinance_headlines()

    def display_bbc_headlines(self):
        # Scraping from bbc
        headlines_bbc = scraper.scrape_bbc()
        for i, headline in enumerate(headlines_bbc):
            title_bbc, link_bbc = headline
            news = scraper.News(title_bbc, link_bbc)

            self.bbc_news_label = ctk.CTkButton(self.bbc_scroll_frame, 
                                            text=news.return_headline(), 
                                            fg_color="gray23",  
                                            hover_color=("gray70", "gray30"), 
                                            font=("Arial", 25),)
            self.bbc_news_label.bind("<Button-1>", lambda event, link=news.return_url(): self.web(link))
            self.bbc_news_label.grid(row=i, pady=5, padx=5, sticky="we")

    def display_yfinance_headlines(self):
        # Scraping from yfinance
        headlines_yfinance = scraper.scrape_yfinance()
        for i, headline in enumerate(headlines_yfinance):
            title_yfinance, link_yfinance = headline
            news = scraper.News(title_yfinance, link_yfinance)

            self.yfinance_news_label = ctk.CTkButton(self.yfinance_scroll_frame, 
                                            text=news.return_headline(), 
                                            fg_color="gray23",  
                                            hover_color=("gray70", "gray30"), 
                                            font=("Arial", 25))
            self.yfinance_news_label.bind("<Button-1>", lambda event, link=news.return_url(): self.web(link))
            self.yfinance_news_label.grid(row=i, pady=5, padx=5, sticky="we")
    
    # Function to open links
    def web(self, url):
        webbrowser.open_new(url)
    
    # Function to implement Frame switching
    def onlift(self):
        self.lift()