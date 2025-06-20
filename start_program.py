from command_list import Commands
from dank_bank import Bank

class StartProgram():
    
    def start(self):
        print("Welcome to Dank Memer Python Edition!\nType \"help\" for list of commands. \n")

        while True:
            try:
                self.command = str(input("Enter a command: "))
                
                if self.command == "help":
                    Commands().show_commands()
                    
                elif self.command == "balance":
                    Bank().show_balance()
                    
                elif self.command == "beg":
                    Commands().beg()
                    
            except ValueError:
                print("Invalid input, try again.")  
                
                
start = StartProgram()
start.start()
