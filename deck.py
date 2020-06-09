import random
import time
from terminal_playing_cards import View
from terminal_playing_cards import Card as Kartu

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        if self.value == 11:
            value = "Jack"
        elif self.value == 12:
            value = "Queen"
        elif self.value == 13:
            value = "King"
        elif self.value == 14:
            value = "Ace"
        else:
            value = self.value
        print(f'{value} of {self.suit}')

    def __gt__(self, other):
        return self.value > other.value

    def show_card_pic(self):
        if self.value == 11:
            value = "J"
        elif self.value == 12:
            value = "Q"
        elif self.value == 13:
            value = "K"
        elif self.value == 14:
            value = "A"
        else:
            value = self.value
        card_in_hand = Kartu(str(value), self.suit)
        hand = View([card_in_hand])
        print(hand)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range (2, 15):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)- 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawcard(self):
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = ''

    def draw(self, deck):
        self.hand = deck.drawcard()
        return self

    def showhand(self):
        self.hand.show()

    def showhand_pic(self):
        self.hand.show_card_pic()
    
    def showplayer(self):
        return self.name

class Table:
    def __init__ (self):
        self.player = ''
        self.deck = Deck()
        self.com = Player("Computer")
    
    def add_player(self):
        # Player.add_player_input()
        name = input("Input your name : ")
        self.player = Player(name)
        return self
    
    def compare_cards(self):
        if self.player.hand > self.com.hand:
            print("you win")
        else:
            print("you lose")

    def computer_draw(self):
        print("Computer draw")
        self.com.draw(self.deck)
        time.sleep(1)
        self.com.showhand_pic()
        self.com.showhand()
    
    def player_draw(self):
        print(f'{self.player.showplayer()} draw')
        self.player.draw(self.deck)
        time.sleep(1)
        self.player.showhand_pic()
        self.player.showhand()

    def start_game(self):
        self.add_player()
        print("=== Shuffling deck ===")
        self.deck.shuffle()
        time.sleep(2)
        self.computer_draw()
        print("======================")
        time.sleep(2)
        self.player_draw()
        print("Comparing")
        print("======================")
        time.sleep(2)
        self.compare_cards()

room = Table()
room.start_game()
while True:
    again = input("Want to play again? (Press 1 to Play again and anything else to exit) : ")
    if again == "1":
        room = Table()
        room.start_game()
    else:
        break



# deck = Deck()
# deck.shuffle()
# p1 = Player("Jack")
# p1.draw(deck)
# p1.showhand()

#     def add_player(self,player):
#         self.players.append(player)

#     def show_player_table(self):
#         for player in self.players:
#             player.showplayer()