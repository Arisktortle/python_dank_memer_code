class PrintCommands():
    
        def show_commands(self):
            print("\n Commands:")
            commands = [
                ("help", "Shows the command list"),
                ("balance", "Show wallet and bank balance"),
                ("shop", "Show items available in the shop"),
                ("buy ITEMNAME", "Buy a specific item in the shop"),
                ("inventory", "Show your inventory"),
                ("bank deposit AMOUNT", "Deposit amount of money"),
                ("bank withdraw AMOUNT", "Withdraw amount of money"),
                ("blackjack", "Play blackjack game"),
            ]
            for cmd, description in commands:
                print(f"   {cmd.ljust(16)} - {description}") # type: ignore
            print()