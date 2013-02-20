#_*_ coding: utf-8 _*_
from game  import Game
from cards import Deck, Card

class Rules(Game):
	"""Rules for the game of 500"""
	def __init__(self):
		super(Rules, self).__init__()
		self.deckStyle = 'French'
		self.deck = Deck(self.deckStyle)
		print self.deck
		self.playerLimit = [4]
		self.gameLimit = 0
		self.roundLimit = 0
		self.handLimit = 0

	def deck(self):
		for cards in [(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(3,3),(0,4),(1,4)]:
			card = Card(self.deckStyle, cards[0], cards[1])
			self.deck.remove(card)

	def dealing(self, players):
		for player in range(self.playerLimit):
			return player


if __name__ == "__main__":
    rules = Rules()