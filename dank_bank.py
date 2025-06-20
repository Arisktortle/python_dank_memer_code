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
        