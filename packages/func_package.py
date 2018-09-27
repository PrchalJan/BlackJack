
# I'm programming the funcitons here

def take_bet(chips):
	chips.bet = 0
	while chips.bet == 0:
		try:
			chips.bet = int(input('How much would you like to bet? 1 - {} '.format(chips.total)))
		except ValueError:
			print('You must enter a number')
		else:
			if chips.bet > chips.total:
				print('Not enough chips!')
				chips.bet = 0
			else:
				print('Player bets {}'.format(chips.bet))


def hit_or_stand(pl_hand, deck)


def display_some(pl_hand, dl_hand):
	print('\n')
	print("Dealer's cards:")
	print("<HIDDEN CARD>")
	print(dl_hand.cards[1])
	print('--------------')
	print("Player's cards:")
	for card in pl_hand.cards:
		print(card)
	print('Value:',pl_hand.value)

