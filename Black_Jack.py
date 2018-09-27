
from packages.classes import class_package as cl
from packages import func_package as fn

#I'm programming the game here	

playing = True


chips = cl.Chips()


while True:
	print('\n'*100)
	print('Welcome to BlackJack')
	print('Get as close to 21 as possible without going over')
	print('Dealer hits until she reaches 17')

	if chips.total == 0:
		chips = cl.Chips()

	deck = cl.Deck()
	deck.shuffle()
	
	player_hand = cl.Hand()
	dealer_hand = cl.Hand()

	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Prompt player to bet
	fn.take_bet(chips)

	fn.display_some(player_hand, dealer_hand)

	while playing:
		

	break

