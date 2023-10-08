import random

class Card(object):
    def __init__(self,suit, val, face_val=None):
        self.suit = suit
        self.value = val
        self.face_val = face_val if face_val is not None else str(val)
    def price(self):
        if self.value >= 10:
            return 10
        elif self.value == 1:
            return 11
        return self.value
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                face_val = None
                if v == 1:
                    face_val = "A"
                elif v == 11:
                    face_val = "J"
                elif v == 12:
                    face_val = "Q"
                elif v == 13:
                    face_val = "K"
                self.cards.append(Card(s, v, face_val))
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
    def drawCard(self, num=1):
        if len(self.cards) < num:
            self.shuffle()  # assuming shuffle method resets and shuffles the deck
        cards = [self.cards.pop() for _ in range(num)]
        return cards if num > 1 else cards[0]
class Player(object):
    def __init__(self, name, isDealer, deck):
        self.name = name
        self.hand = []
        self.isDealer = isDealer
        self.cash = 100
        self.score = 0
    def drawShow(self, deck):
        drawn_card = deck.drawCard()
        self.hand.append(drawn_card)
        self.score = self.check_score()
        print(f"{drawn_card.face_val} of {drawn_card.suit}")
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        self.score = self.check_score()
    def check_score(self):
        a_counter = 0
        self.score = 0
        for card in self.hand:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()
        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score
    def place_bet(self, bet):
        if self.cash >= bet:
            self.cash -= bet
            return True  # Successful bet placement
        else:
            return False  # Failed to place bet due to insufficient cash

