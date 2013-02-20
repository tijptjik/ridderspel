#_*_ coding: utf-8 _*_
from random import choice, shuffle

deckStyles = {
	'French' : {
		'suitSymbols' 		: [u'♥',u'♦',u'♣',u'♠'],
		'suitAltSymbols' 	: [u'♡',u'♢',u'♧',u'♤'],
		'suitUnicodes'		: ['1F0B','1F0C','1F0D','1F0A'],
		'suitNames' 		: ['Hearts','Diamonds','Clubs','Spades'],
		'rankNames' 		: [None,'Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King'],
		'rankSymbols' 		: [None,'1','2','3','4','5','6','7','8','9','10','J','R','Q','K'],
	},
	'Knightly' : {
		'suitSymbols' 		: [u'♥',u'♦',u'♣',u'♠'],
		'suitAltSymbols' 	: [u'♡',u'♢',u'♧',u'♤'],
		'suitUnicodes'		: ['1F0B','1F0C','1F0D','1F0A'],
		'suitNames' 		: ['Hearts','Diamonds','Clubs','Spades'],
		'rankNames' 		: [None,'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Knight','Queen','King'],
		'rankSymbols' 		: [None,'1','2','3','4','5','6','7','8','9','10','J','C','Q','K'],
	}
}

specialCards = {
	'Jokers' : {
		'suitSymbols' 		: [u'🃏'],
		'suitAltSymbols' 	: [u'🃟'],
		'suitNames' 		: ['Joker'],
		'rankNames' 		: None,
		'rankSymbols' 		: None,
	}
}

class Deck(object):
	"""A Deck of Playing Cards"""
	def __init__(self, deck='French'):
		super(Deck, self).__init__()
		self.cards = []
		for suit in range(len(deckStyles[deck]['suitNames'])):
			for rank in range(1, len(deckStyles[deck]['rankNames'])):
				self.cards.append(Card(deck,suit, rank))

	def remove(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return True
		return False

	def shuffle(self):
		random.shuffle(self.cards)


class Card(object):
	"""A Playing Card"""
	def __init__(self, deck, suit=0, rank=1):
		super(Card, self).__init__()
		self.suit = suit
		self.rank = rank
		self.suitName = deckStyles[deck]['suitNames'][suit]
		self.suitSymbol = deckStyles[deck]['suitSymbols'][suit]
		self.rankName = deckStyles[deck]['rankNames'][rank]
		if deckStyles[deck]['suitUnicodes']:
			if deck == 'French' and rank > 11:
				rank = rank + 1
			self.unicode = unicode(unichr(int(deckStyles[deck]['suitUnicodes'][suit] + unicode(hex(rank)[2].upper()),16)))
	def __str__(self):
		return str(self.rankName) + ' of ' + str(self.suitName)
	def __unicode__(self):
		return (self.unicode if self.unicode else self.suit + self.rank)
	# def _cmp_():


if __name__ == "__main__":
    deck = Deck('French')
    for card in deck.cards:
    	print card