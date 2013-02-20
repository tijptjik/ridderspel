#_*_ coding: utf-8 _*_

class Game(object):
	"""docstring for Game"""
	games = {'fivehundred' : '500', 'ohhell': 'Oh Hell!'}
	def __init__(self):
		super(Game, self).__init__()
		n = 1
		selection = []
		for game, name in self.games.iteritems():
			print str(n) + ') ' + name
			n = n + 1
			selection.append(game)
		load = input('\n Please select your game.\n  ')
		self.game = __import__(selection[int(load) - 1].Rules)
		self.deck = self.game.deck()
		self.playerLimit = self.game.playerLimit[]
		self.gameLimit = self.game.gameLimit[]
		self.roundLimit = self.game.roundLimit[]
		self.handLimit = self.game.handLimit[]

	
	def deal(self):
		self.deck.shuffle()



if __name__ == "__main__":
    play = Game()