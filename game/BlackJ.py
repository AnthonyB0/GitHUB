from deck2 import Deck
from deck2 import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.player = Player("Player", False,self.deck)
        self.dealer = Player("Dealer", True, self.deck)

    def play(self):
        playing = True
        while playing:
            self.deck.shuffle()
            bet = self.get_bet_amount(self.player.cash)
            self.player.place_bet(bet)
            self.player.draw(self.deck)
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
            self.dealer.draw(self.deck)

            while True:
                print("Players hand: ", end="")
                for card in self.player.hand:
                    print(f"{card.face_val} ", end="")
                print()
                print(f"Players Score: {self.player.score}")

                print("Dealer's showing card: ", end="")
                print(f"{self.dealer.hand[0].face_val} of {self.dealer.hand[0].suit}")

                move = input("Do you want to [H]it, [S]tand, [D]ouble down, or [Q]uit? ").lower()

                if move == 'h':
                    self.player.drawShow(self.deck)
                    if self.player.check_score() > 21:
                        print("Bust! You lose.")
                        self.bet = 0
                        break
                elif move == 's' or move == 'd':
                    if move == 'd':
                        if self.player.cash >= bet:  # Check if the player has enough cash to double down.
                            self.player.place_bet(bet)
                            bet = bet * 2
                        else:
                            print("Insufficient Funds, Lets hit the deck.")
                        print(f"You hit ")
                        self.player.drawShow(self.deck)
                        if self.player.check_score() > 21:
                            print("Bust! You lose.")
                            bet = 0
                            break
                    while self.dealer.check_score() < 17:
                        print(f"Dealer hit ")
                        self.dealer.drawShow(self.deck)
                    print("Dealer's hand: ", end="")
                    for card in self.dealer.hand:
                        print(f"{card.face_val} ", end="")
                    print()
                    print(f"Dealer: {self.dealer.score}")
                    if self.dealer.score > 21 or self.dealer.score < self.player.score:
                        print("You win!")
                        self.player.cash += bet*2
                        bet = 0
                    elif self.dealer.score < self.player.score:
                        print("You lose!")
                        bet = 0
                    elif self.dealer.score == self.player.score:  # This condition checks for a tie
                        print("It's a tie! You get your bet back.")
                        self.player.cash += bet  # Player gets their bet back
                    break
                elif move == 'q':
                    playing = False
                    break
                else:
                    print("Invalid move, please try again.")
            if self.player.cash <= 0:
                print("You are out of cash! Game over.")
                break

            # Resetting for next game
            self.player.hand = []
            self.dealer.hand = []

            play_again = input("Do you want to play again? [Y/N] ").lower()
            if play_again != 'y':
                playing = False


    def get_bet_amount(self, pcash):
        while True:
            bet = input(f"You have ${pcash}. How much would you like to bet? ")
            try:
                bet = int(bet)
                if bet <= pcash and bet > 0:
                    return bet
                else:
                    print("Invalid bet amount. Please bet a positive amount and no more than you have.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")