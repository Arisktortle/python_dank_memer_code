import random

class PlayerHand:
    def __init__(self):
        self.hand = []
        
    def draw_card(self):
        card = random.randint(2,11)
        self.hand.append(card)
        
    def total_cards(self):
        return sum(self.hand)
    
    def show(self):
        print(f"Total cards: {self.total_cards()}")
        
class BlackJackLogic:
    def __init__(self):
        self.dealer = PlayerHand()
        self.player = PlayerHand()
        
    def play(self):
        for draw_count in range(2):
            self.player.draw()
            self.dealer.draw()
            
 
    