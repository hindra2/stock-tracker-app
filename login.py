import json
import pandas as pd


class Login:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

        self.information_file_path = "./users.json"
        self.information_file = open(self.information_file_path, "w")

    def saveLoginInfo(self):
        with open(self.information_file_path, 'a') as f:
            f.write("\n" + self.username + "," + self.password)

    def validate_login(self, username, password):
        with open(self.information_file_path, 'r') as f:
            readable = f.read()
            lines = readable.splitlines()
            user = list(filter(lambda l: l.split(',')[0] == self.username and l.split(',')[1] == self.password, lines))
            if user:
                print("Login successful")
            else:
                print("Login failed. Wrong Username or Password.")
            f.close()