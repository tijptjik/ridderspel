#_*_ coding: utf-8 _*_
from game  import Game, Player
from cards import Deck, Card
from math import floor, ceil

class Rules(Game):
	"""Rules for the game of Oh Hell!"""
	def __init__(self):
		self.deckStyle = 'French'
		self.deck = Deck(self.deckStyle)
		self.playerLimit = [3,4,5,6,7]
		self.handLimit = [11,13,15,17,19,21,23]
		super(Rules, self).__init__()
		self.handCounter = 0
		self.hands = [Hand(n, self.handLimit) for n in range(self.handLimit)]
	
	def limitHands(self):
		i = 1
		while self.playerLimit * i < len(self.deck.cards):
			print i
			i = i + 1
			# pass
		self.handLimit = 'xx'

	def setupDeck(self):
		for cards in [(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(3,3),(0,4),(1,4)]:
			card = Card(self.deckStyle, cards[0], cards[1])
			self.deck.remove(card)

	def deal(self):
		self.setupDeck()
		self.deck.shuffle()
		cards = self.deck.cards
		for player in self.players:
			for n in range(self.hands[self.handCounter].cardLimit):
				player.hand.append(cards.pop())

		for player in self.players:
			print str(player), ':'
			holding = u""
			for card in player.hand:
				holding = holding + card.__unicode__() + '  '
			print holding
		print '\n\n\n'

class Hand(object):
	"""The parameters for the respective hands played throughout the games.
	   
	   In the case of 'Oh Hell' the number of cards dealt in each hand fluctuates
	   throughout the game, as does the trump suit. Depending on the variant and
	   number of players, the game generally starts with 8 cards per player, 
	   diminising by one each hand until 1 card per player remains. The following 
	   hands each add another card to the players' hands until the original number
	   is reached. 
   
	   Trumps proceed from Spades, Diamons, Clubs, Hearts to No Trumps"""
	def __init__(self, n, handLimit):
		super(Hand, self).__init__()
		self.trumpSuits = [u'♠',u'♦',u'♣',u'♥',None]
		self.counter = n
		self.trump = n % 5
		if n > int(floor(float(handLimit)/2.0)):
			n = n + 2
		self.cardLimit = abs(int(ceil(float(handLimit)/2.0)) - n)
	def __str__(self):
		return 'Hand ' + str(self.counter) + ':' + ' ' + str(self.cardLimit) + ' ' + str(self.trump)
	def __unicode__(self):	
		return 'Hand ' + str(self.counter) + ':' + ' ' + str(self.cardLimit) + ' ' + str(self.trumpSuits[self.trump])


if __name__ == "__main__":
    rules = Rules()