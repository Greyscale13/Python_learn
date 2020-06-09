from terminal_playing_cards import View
from terminal_playing_cards import Card as Kartu

ace_hearts = Kartu("8", "spades", value=1)
hand = View([ace_hearts])
print(hand)