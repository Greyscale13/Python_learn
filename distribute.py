#     def distribute_cards(self,deck):
#         while len(deck.cards) > 0:
#             for player in self.players:
#                 player.draw(deck)

    # def __repr__ (self):
    #     if self.value == 11:
    #         value = "Jack"
    #     elif self.value == 12:
    #         value = "Queen"
    #     elif self.value == 13:
    #         value = "King"
    #     elif self.value == 1:
    #         value = "Ace"
    #     else:
    #         value = self.value
    #     return f'{value} of {self.suit}'

    # while True:
#     name = input("Enter your name : ")
#     country = input("Enter your origin : ")
#     pp = Player(name,country)
#     table.add_player(pp)
#     add = input("Press 1 to add more players, 2 to see players, and 0 to exit : ")
#     if add == '1':
#         pp.showplayer()
#         continue
#     elif add == '2':
#         table.show_player_table()
#         continue
#     else:
#         break

# table = Table()

# p1 = Player("Jack")
# table.add_player(p1)
# p2 = Player("Allison")
# table.add_player(p2)
# p3 = Player("Dunder")
# table.add_player(p3)
# p4 = Player("Kalen")
# table.add_player(p4)

# table.distribute_cards(deck)
# table.show_player_table()