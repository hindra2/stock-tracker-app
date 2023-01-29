import customtkinter as ctk
import login
import mainPage

class LoginPage(ctk.CTk):
    def __init__(self):
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
        
        self.validation_label = ctk.CTkLabel(master=self, text="", font=("Arial", 15))
        self.validation_label.grid(column=0, row=2, columnspan=2, padx=50, pady=5, sticky="we")

        self.login_button = ctk.CTkButton(master=self,
                                          text="Login",
                                          command=self.login,
                                          font=("Arial", 15))
        self.login_button.grid(column=0, row=3, columnspan=2, padx=50, pady=50, sticky="nswe")

    def onlift(self):
        self.lift()

    def write_login(self):
        username = self.user_username.get()
        password = self.user_password.get()
        user_instance = login.Login(username, password)
        user_instance.saveLoginInfo()

    def login(self):
        self.username = self.user_username.get()
        self.password = self.user_password.get()
        if login.validate_login(self.username, self.password):
            self.destroy()
            app = mainPage.MainApp()
            app.mainloop()
        else:
            self.validation_label.configure(text="Invalid Login Info!")


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()