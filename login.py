# Library Imports
import pickle
import os

# Specify Database Path relative to os
database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "users")


# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # Getter Function
    def get_username(self):
        return self.username

    # Pickles user data
    def store_login(self):
        try:
            user_info = {self.username: self.password}

            database = open("users", "ab")
            pickle.dump(user_info, database)
            database.close()
        except:
            pass

    # Validates if user data is in pickle database
    def validate_login(self):
        try:
            with open(database_path, 'rb') as f:
                try:
                    # Loops checking of username and password to see if there is a valid combination in the database, return True if found
                    while True:
                        data = pickle.load(f)
                        if isinstance(data, dict) and self.username in data and data[self.username] == self.password:
                            return True
                # Stops while loop after finishing checking the entire database and returns False
                except EOFError:
                    pass
                return False

        # Error handling for corrupt data or file not found
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error loading data: {e}")
            return False
        
        # Closes the database
        finally:
            f.close()