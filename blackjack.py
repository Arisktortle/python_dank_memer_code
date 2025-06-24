import random

class BlackjackGame:
    def __init__(self):
        self.hand = []
        
    def draw_card(self):
        card = random.randint(2,11)
        self.hand.append(card)
        
    def total_cards(self):
        return sum(self.hand)
    
    def show(self):
        print(f"Total cards: {self.total_cards()}")