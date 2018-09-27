
from packages import func_package
from packages.classes import class_package

#I'm programming the game here	

playing = True

chips = Chips()

while True:
	print('\n*100')
	print('Welcome to BlackJack')
	print('Get as close to 21 as possible without going over')
	print('Dealer hits until she reaches 17')

	if chips == 0:
		chips = Chips()

	deck = Deck()

