from command_list import PrintCommands

class StartProgram():
    
    def start(self):
        print("Welcome to Dank Memer Python Edition!\nType \"help\" for list of commands. \n")

        while True:
            try:
                self.command = str(input("Enter a command: "))
                
                if self.command == "help":
                    PrintCommands().show_commands()
            
            
            except ValueError:
                print("Invalid input, try again.")  
                
start = StartProgram()
start.start()
