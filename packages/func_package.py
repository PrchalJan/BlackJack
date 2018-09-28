
# I'm programming the funcitons here

playing = True

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
				print('\n'*100)
				print('Player bets {}'.format(chips.bet))

def take_hit(hand, deck):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()


def hit_or_stand(pl_hand, deck):
	global playing

	while True:
		x = input("Do you wish to hit or stand? ('h' or 's') ")
		if x[0].lower() == 'h':
			take_hit(pl_hand, deck)
		elif x[0].lower() == 's':
			print('Player stands, dealer goes!')
			playing = False
		else:
			print('I did not understand that. Try again!')
		break


def display_some(pl_hand, dl_hand):
	print('\n')
	print("Dealer's cards:")
	print("<HIDDEN CARD>")
	print(dl_hand.cards[1])
	print('--------------')
	print("Player's cards:")
	for card in pl_hand.cards:
		print(card)
	print('Your current value is:',pl_hand.value)

def display_all(pl_hand, dl_hand):
	print('\n')
	print("Dealer's cards:")
	for card in dl_hand.cards:
		print(card)
	print("Dealer's hand value is:", dl_hand.value)
	print('--------------')
	print("Player's cards:")
	for card in pl_hand.cards:
		print(card)
	print("Player's hand value is:", pl_hand.value)
	print('')


def player_busts(chips):
	chips.lose_bet()
	print('')
	print('Player busts!')

def player_wins(chips):
	chips.win_bet()
	print('Player wins!')

def dealer_busts(chips):
	chips.win_bet()
	print('Dealer busts. Player wins!')

def dealer_wins(chips):
	chips.lose_bet()
	print('Dealer wins!')

def push(chips):
	chips.bet = 0
	print('This game is a draw!')

def play_again():
	while True:
		print('')
		play = input("Do you wish to play again? 'y' or 'n'")
		if play[0].lower() == 'y':
			return True
		elif play[0].lower() == 'n':
			return False
		else:
			print('I did not understand that "y" or "n"')

