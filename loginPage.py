# Library Imports
import customtkinter as ctk
import login
import mainPage

# Login Window class
class LoginPage(ctk.CTk):
    def __init__(self):
        # To inherit properties of CTk parent class
        super().__init__()
        self.title("Login Page")

        # Configuring Grid
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        # UI Elements For Login Page
        self.username_label = ctk.CTkLabel(master=self, text="Username:", font=("Arial", 15))
        self.username_label.grid(column=0, row=0, padx=50, pady=25, sticky="we")

        self.user_username = ctk.CTkEntry(master=self, font=("Arial", 15))
        self.user_username.grid(column=1, row=0, padx=50, pady=25, sticky="we")

        self.password_label = ctk.CTkLabel(master=self, text="Password:", font=("Arial", 15))
        self.password_label.grid(column=0, row=1, padx=50, pady=25, sticky="we")

        self.user_password = ctk.CTkEntry(master=self, font=("Arial", 15), show="*")
        self.user_password.grid(column=1, row=1, padx=50, pady=25, sticky="we")
        
        self.validation_label = ctk.CTkLabel(master=self, text="", font=("Arial", 1))
        self.validation_label.grid(column=0, row=2, columnspan=2, padx=50, pady=5, sticky="we")

        self.new_user_checkbox = ctk.CTkCheckBox(master=self, 
                                                text="New User", 
                                                font=("Arial", 15), 
                                                onvalue="on", 
                                                offvalue="off")
        self.new_user_checkbox.grid(column=0, row=3, columnspan=2, padx=50, pady=5, sticky="nswe")

        self.login_button = ctk.CTkButton(master=self,
                                          text="Login",
                                          command=self.login,
                                          font=("Arial", 15))
        self.login_button.grid(column=0, row=4, columnspan=2, padx=50, pady=50, sticky="nswe")

    # Login Function
    def login(self):
        # Gets value of username and password from text entry and stores it into variables
        username = self.user_username.get()
        password = self.user_password.get()

        # Creates User instance
        user = login.User(username, password)

        # Checks if it is a new user or not
        if self.new_user_checkbox.get() == "off":

            # Checks if login info is valid
            if user.validate_login():
                self.destroy()
                app = mainPage.MainApp(user)
                app.mainloop()
            else:
                # Alerts user of wrong login info
                self.validation_label.configure(text="Invalid Login Info!")
        else:
            # Calls store_login to store user data if it is a new user
            user.store_login()