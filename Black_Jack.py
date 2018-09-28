
from packages.classes import class_package as cl
from packages import func_package as fn

#I'm programming the game here	


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

	fn.playing = True

	while fn.playing:
		fn.hit_or_stand(player_hand, deck)
		print('\n'*100)
		fn.display_some(player_hand, dealer_hand)
		if player_hand.value > 21:
			fn.player_busts(chips)
			fn.playing = False
	
	if player_hand.value <= 21:	
		while dealer_hand.value < 17:
			fn.take_hit(dealer_hand, deck)

		print('\n'*100)
		fn.display_all(player_hand, dealer_hand)

		if dealer_hand.value > 21:
			fn.dealer_busts(chips)
		elif player_hand.value > dealer_hand.value:
			fn.player_wins(chips)
		elif player_hand.value < dealer_hand.value:
			fn.dealer_wins(chips)
		else:
			fn.push(chips)
	print("Player's winnings stand at {}".format(chips.total))
	if fn.play_again():
		continue
	else:
		print('\n'*100)
		print("Thanks for playing")
	break

