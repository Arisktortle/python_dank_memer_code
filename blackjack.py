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
            self.player.draw_card()
            self.dealer.draw_card()
            
        self.player.show()
        
        while self.player.total_cards() <= 21:
            user_move = input("hit or stand?: ").lower()
            if user_move == "hit":
                self.player.draw()
                self.player.show()
            else:
                break
            
        if self.player.total_cards() > 21:
            print("Busted. The dealer wins.")
            return
            
        print("\nDealer's turn:")
        self.dealer.show()
        while self.dealer.total_cards() < 17:
            self.dealer.draw_card()
            self.dealer.show()
            
        self.show_result()
            
    def show_result(self):
        player_total = self.player.total_cards()
        dealer_total = self.dealer.total_cards()
        print("\n--- Final ---")
        print(f"You:    {len(self.player.hand)} cards | Total: {player_total}")
        print(f"Dealer: {len(self.dealer.hand)} cards | Total: {dealer_total}")
        
        if dealer_total > 21 or player_total > dealer_total:
            print("You win!")
        elif player_total == dealer_total:
            print("Tie!")
        else:
            print("Dealer wins.")
        
            
            
                
 
    