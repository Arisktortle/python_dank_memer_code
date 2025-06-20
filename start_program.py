from command_list import Commands
from user_data import UserData
from dank_bank import Bank

class StartProgram():
    def __init__(self):
        self.user_data = UserData()
        self.account = self.user_data.load_data()
        self.commands = Commands(self.account)
        
    def start(self):
        print("Welcome to Dank Memer Python Edition!\nType \"help\" for list of commands. \n")

        while True:
            try:
                command = (input("Enter a command: "))
                
                if command == "help":
                    Commands().show_commands()
                    
                elif command == "balance":
                    Bank().show_balance()
                    
                elif command == "beg":
                    Commands().beg()
                    
            except ValueError:
                print("Invalid input, try again.")  
                
start = StartProgram()
start.start()
