
# I'm programming the classes here.

suits = ('Spades', 'Diamodns', 'Clubs', 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,\
		 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[self.rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit





class Deck():
	def __init__(self):
		self.cards = []

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0