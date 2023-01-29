import tkinter as tk

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("300x150")

        # create widgets
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.check_credentials)

        # create layout
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # check if the entered credentials match the hardcoded ones
        if username == "admin" and password == "admin":
            self.destroy()
            success_page = tk.Tk()
            success_page.title("Success")
            success_page.geometry("200x50")
            success_label = tk.Label(success_page, text="Login successful!")
            success_label.pack()
            success_page.mainloop()
        else:
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            error_label = tk.Label(self, text="Invalid credentials")
            error_label.pack()

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()