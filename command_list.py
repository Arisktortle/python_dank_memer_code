import random
import time

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
        
    def set_cooldown(self, command_name, cooldown_seconds):
        current_time = time.time()
        last_used = self.account.cooldowns.get(command_name, 0)
        
        if current_time - last_used < cooldown_seconds:
            time_left = int(cooldown_seconds - (current_time - last_used))
            return True, time_left
        else:
            self.account.cooldowns[command_name] = current_time
            return False, 0
        
    def beg(self):
        cooldown_active, seconds_left = self.set_cooldown("beg", 30)
        if cooldown_active:
            return f"This command has a cooldown, try again in {seconds_left} seconds."
        
        amount = random.randint(1, 100)
        self.account.wallet += amount
        donators = ["a kind stranger", "a wizard", "Elon Musk", "an NPC", "Sara Duterte", "a dog", "Gelo Cruz"]
        donor = random.choice(donators)
        return f"\n{donor} gave you ${amount}...\n"
