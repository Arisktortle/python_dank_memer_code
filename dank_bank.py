class Bank:
    def __init__(self, data=None):
        if data:
            self.wallet = data.get("wallet", 1000)
            self.bank= data.get("bank", 0)
            self.inventory = data.get("inventory", [])
        else:
            self.wallet = 1000
            self.bank = 0 
            self.inventory = []
            
    def to_dict(self):
        return {
            "wallet": self.wallet,
            "bank": self.bank,
            "inventory": self.inventory
        }
        
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if self.wallet >= amount:
            self.wallet -= amount
            self.bank += amount
            return f"Sucessfully deposited ${amount} to your bank."
        return "Not enough balance in wallet."
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive."
        if self.bank >= amount:
            self.bank -= amount
            self.wallet += amount
            return f"Successfully withdrawn ${amount} from your bank."
        return "Not enough balance in bank."
    
    def show_balance(self):
        return f"Wallet: ${self.wallet} | Bank: ${self.bank}"
