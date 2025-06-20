class StartProgram():
    
    def start(self):
        print("Welcome to Dank Memer Python Edition!")
        
        while True:
            try:
                self.command = str(input("Type \"help\" for list of commands.\n Enter a command: "))
                continue
            
            except ValueError:
                print("Invalid input, try again.")  