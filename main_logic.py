from command_list import Commands
from user_data import UserData
from dank_bank import Bank

class StartProgram():
    def __init__(self):
        username = input("Enter your username: ").strip().lower()
        self.user_data = UserData(username)
        self.account = self.user_data.load_data()
        self.commands = Commands(self.account)
        
    def start(self):
        print("\nWelcome to Dank Memer Python Edition!\nType \"help\" for list of commands. \n")

        while True:
            try:
                command = (input("Enter a command: "))
                
                if command == "help":
                    self.commands.show_commands()
                    
                elif command == "balance":
                    print(self.account.show_balance())
                    
                elif command == "beg":
                    print(self.commands.beg())
                    self.user_data.save(self.account)
                    
                elif command == "exit":
                    self.user_data.save(self.account)
                    print("Game saved. Thank you for using the program!")
                    break
                
                elif command.startswith("bank deposit"):
                    try:
                        amount = int(command.split()[2])
                        print(self.commands.deposit(amount))
                        self.user_data.save(self.account)
                    except:
                        print("Usage: bank deposit AMOUNT")

                elif command == "blackjack":
                    self.commands.blackjack()
                    self.user_data.save(self.account)
                    
            except ValueError:
                print("Invalid command, type 'help' for list of commands.")
                
start = StartProgram()
start.start()
