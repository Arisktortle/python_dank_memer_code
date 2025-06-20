import random

class Commands():
    def __init__(self, account):
        self.account = account
    
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
            
    def beg(self):
        amount = random.randint(1, 100)
        self.account.wallet += amount
        donators = ["a kind stranger", "a wizard", "Elon Musk", "an NPC", "Sara Duterte", "a dog", "Gelo Cruz"]
        donor = random.choice(donators)
        return f"{donor} gave you ${amount}..."
