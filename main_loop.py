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
            