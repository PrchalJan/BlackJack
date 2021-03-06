
# I'm programming the classes here.
import random

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
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit,rank))

	def __str__(self):
		comp = ''
		for card in self.cards:
			comp = comp + '\n' + card.__str__()
		return 'The deck has: \n' + comp

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		return self.cards.pop()


class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1



class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def lose_bet(self):
		self.total -= self.bet
		self.bet = 0

	def win_bet(self):
		self.total += self.bet
		self.bet = 0