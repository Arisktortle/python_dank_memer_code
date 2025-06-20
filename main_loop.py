import json
import os

class MainLoop:
    def __init__(self, data_file="data.json"):
        self.user  = None
        self.data_file = data_file
        self.command = None
        self.store_items
        
    def start(self):
        print("Welcome to Dank Memer Python Edition!")
        
        while True:
            try:
                self.command = str(input("Type \"help\" for list of commands.\n Enter a command: "))
                continue
            
            except ValueError:
                print("Invalid input, try again.")  
                
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.user_data, f, indent=4)
            
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
    
            