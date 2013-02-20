#_*_ coding: utf-8 _*_

class Game(object):
	"""docstring for Game"""
	games = {
		'fivehundred' 	: '500', 
		'ohhell'		: 'Oh Hell!'
		}
	def __init__(self):
		super(Game, self).__init__()
		self.game = self.selectGame()
		self.playerNumber = self.selectNumberOfPlayers()
		self.deal()

	def selectGame(self):
		n = 1
		selection = []
		print 'Select your game: \n'
		for game, name in self.games.iteritems():
			print str(n) + ') ' + name
			n = n + 1
			selection.append(game)
		load = input('\n')
		return __import__(selection[int(load) - 1].Rules)
	
	def selectNumberOfPlayers(self):
		if len(self.playerLimit) == 1:
			return self.playerLimit[0]
		else:
			print 'Game allows for', self.playerLimit, 'players'
		playerNumber = input('\n How many players are joining?\n')
		if playerNumber in self.playerLimit:
			return playerNumber
		else:
			print 'You must select a number within', self.playerLimit, '\n'
			selectNumberOfPlayers(self)

	def deal(self):
		self.deck.shuffle()



if __name__ == "__main__":
    print "\
______  _      _      _              _____               _ \n\
| ___ \(_)    | |    | |            /  ___|             | |\n\
| |_/ / _   __| |  __| |  ___  _ __ \ `--.  _ __    ___ | |\n\
|    / | | / _` | / _` | / _ \| '__| `--. \| '_ \  / _ \| |\n\
| |\ \ | || (_| || (_| ||  __/| |   /\__/ /| |_) ||  __/| |\n\
\_| \_||_| \__,_| \__,_| \___||_|   \____/ | .__/  \___||_|\n\
                                           | |             \n\
                                           |_|             "

    play = Game()