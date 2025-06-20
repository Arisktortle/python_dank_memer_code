from dank_bank import Bank
import os
import json

class UserData:
    def __init__(self, username):
        self.username = username
        self.data_file = f"data_{username}.json"
        
    def load_data(self):
        if not os.path.exists(self.data_file):
            print(f"\nNew user '{self.username}'. Creating a new profile...\n")
            return Bank()
        print(f"Good to see you again, {self.username}!")
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        return Bank(data=data)
    
    def save(self, account: Bank):
        with open(self.data_file, 'w') as f:
            json.dump(account.to_dict(), f, indent=4)