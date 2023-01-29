import json
import os

json_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "users.json")

def validate_login(username, password):
    with open(json_path, 'r') as f:
        users = json.load(f)
    
    if username in users and users[username] == password:
        return True