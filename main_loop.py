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
            
    def command_list(self):
        print("\n Commands:")
        commands = [
            ("help", "Shows the command list")
            ("balance", "Show wallet and bank balance")
            ("shop", "Show items available in the shop")
            ("buy ITEMNAME", "Buy a specific item in the shop")
            ("inventory", "Show your inventory")
            ("bank deposit AMOUNT", "Deposit amount of money")
            ("bank withdraw AMOUNT", "Withdraw amount of money")
            ("blackjack", "Play blackjack game")
        ]
        for cmd, description in commands:
            print(f"   {cmd.ljust(16)} ---> {description}") # type: ignore
        print()
            