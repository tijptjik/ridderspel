#_*_ coding: utf-8 _*_
from importlib import import_module

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.gameLimit = 0
		self.roundLimit = 0
		self.handLimit = 0
		self.playerNumber = self.selectNumberOfPlayers()
		self.players = [Player(n) for n in range(self.playerNumber)]

	def selectNumberOfPlayers(self):
		players = self.playerLimit
		if len(players) == 1:
			return players[0]
		else:
			print 'Game allows for', players, 'players'
		playerNumber = input('\n How many players are joining?\n')
		if playerNumber in players:
			print
			return playerNumber
		else:
			print 'You must select a number within', players, '\n'
			self.selectNumberOfPlayers()
	
	def newGame(self):
		self.__init__()

	def deal(self):
		self.deck.shuffle()
		print self.deck

class GameLoader(object):
	"""docstring for GameLoader"""
	games = {
		'fivehundred' 	: '500', 
		'ohhell'		: 'Oh Hell!'
		}
	def __init__(self):
		super(GameLoader, self).__init__()
		self.game = self.selectGame()
		self.loadGame()

	def selectGame(self):
		n = 1
		selection = []
		print 'Select your game: \n'
		for game, name in self.games.iteritems():
			print str(n) + ') ' + name
			n = n + 1
			selection.append(game)
		load = input('\n')
		loaded = import_module('games.' + selection[int(load) - 1]) 
		return loaded.Rules()

	def loadGame(self):
		return self.game
		
class Player(object):
	"""docstring for Player"""
	playerNames = ['Maru 8','Schmoka','Goya']
	def __init__(self, n):
		super(Player, self).__init__()
		self.id = n
		self.hand = []
	def __str__(self):
		return self.playerNames[self.id]
		

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
    loader = GameLoader()
    play = loader.loadGame()
    play.deal()