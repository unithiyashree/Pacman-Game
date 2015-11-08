from random import randint

def create_game():
	# Creating the board.
	board = [[ '.' for a in range(35)] for b in range(15)]
	p = randint(1, 13)

	# making walls on the board..!!!
	for j in range (0, 15):
		board[j][0] = 'X'
		board[j][34] = 'X'
	for j in range(0, 35):
		board[0][j] = 'X'
		board[14][j] = 'X'
	for j in range(4, 10):
		board[j][p] = 'X'
	for j in range(10, 25):
		board[p][j] = 'X'
	
	# Intializing the variables
	coin_count = 0
	ghost1 = 0
	ghost2 = 0
	ghost3 = 0 
	pacman = 0
	
	# Filling the coins on the board. 
	while coin_count != 30:
		x = randint(1, 14)
		y = randint(1, 34)
		if board[x][y] == '.':
			board[x][y] = 'C'
			coin_count = coin_count + 1
	
	# Placing the ghost on the board		
	while ghost1 != 1:
		x = randint(1, 14)
		y = randint(1, 34)
		if board[x][y] == '.':
			board[x][y] = 'G'
			ghost1 = ghost1 + 1
		ghost1_pos = [x, y]
	
	# Placing the 2nd ghost on the board		
	while ghost2 != 1:
		x = randint(1, 14)
		y = randint(1, 34)
		if board[x][y] == '.':
			board[x][y] = 'G'
			ghost2 = ghost2 + 1
		ghost2_pos = [x, y]
	
	# Placing the 3rd ghost on the board		
	while ghost3 != 1:
		x = randint(1, 14)
		y = randint(1, 34)
		if board[x][y] == '.':
			board[x][y] = 'G'
			ghost3 = ghost3 + 1
		ghost3_pos = [x, y]
	
	# Placing the pacman on the board.
	while pacman != 1:
		x = randint(1, 14)
		y = randint(1, 34)
		if board[x][y] == '.':
			board[x][y] = 'P'
			pacman = pacman + 1
		pacman_pos = [x, y]	
	return [ghost1_pos, pacman_pos, board, ghost2_pos, ghost3_pos]

class person():
	def __init__(self, e):
		self.e = e
		self.state = True

class pacman(person):
	
	def __init__(self, x, y, e, board):
		person.__init__(self, e)
		self.x = x
		self.y = y
		self.e = e
		self.board = board
		self.state = 0
	
	# Checking the empty position for the movement of pacman
	def checkPlace(self):
		if  self.e == 'w' and self.board[self.x-1][self.y] == '.':
				self.board[self.x][self.y] = '.'
				if self.x-1 < 0 :
					self.board[14][self.y] = 'P'
					pos[1][0] = 14
					pos[1][1] = self.y
				else:
					self.board[self.x-1][self.y] = 'P'
					pos[1][0] = self.x-1
					pos[1][1] = self.y
		if self.e == 's' and self.board[self.x+1][self.y] == '.':
				self.board[self.x][self.y] = '.'
				if self.x+1 > 14 :
					self.board[0][self.y] = 'P'
					pos[1][0] = 0
					pos[1][1] = self.y
				else:	
					self.board[self.x+1][self.y] = 'P'
					pos[1][0] = self.x+1
					pos[1][1] = self.y
		if self.e == 'a' and self.board[self.x][self.y-1] == '.':
				self.board[self.x][self.y] = '.'
				if self.y-1 < 0 :
					self.board[self.x][34] = 'P'
					pos[1][0] = self.x
					pos[1][1] = 34
				else:	
					self.board[self.x][self.y-1] = 'P'
					pos[1][0] = self.x
					pos[1][1] = self.y-1
		if self.e == 'd' and self.board[self.x][self.y+1] == '.':
				self.board[self.x][self.y] = '.'
				if self.y+1 > 34:
					self.board[self.x][0] = 'P'
					pos[1][0] = self.x
					pos[1][1] = 0
				else:	
					self.board[self.x][self.y+1] = 'P'
					pos[1][0] = self.x
					pos[1][1] = self.y+1

	# Checking empty position for the movement of the Ghost
	def checkGhost(self):
		global state1
		if self.e == 'w' and self.board[self.x-1][self.y] == 'G':
			state1 = 1
			print state1
		if self.e == 's'and self.board[self.x+1][self.y] == 'G':
			state1 = 1
			print state1
		if self.e == 'a' and self.board[self.x][self.y-1] == 'G':
			state1 = 1
			print state1
		if self.e == 'd' and self.board[self.x][self.y+1] == 'G':
			state1 = 1
			print state1
	
	# Updating the total coins
	def collectCoins(self):
		global coins
		if self.e == 'w'and self.board[self.x-1][self.y] == 'C':
				self.board[self.x-1][self.y] = 'P'
				self.board[self.x][self.y] = '.'
				coins = coins + 1
				pos[1][0] = self.x-1
				pos[1][1] = self.y
		if self.e == 's' and self.board[self.x+1][self.y] == 'C':
				self.board[self.x+1][self.y] = 'P'
				self.board[self.x][self.y] = '.'
				coins = coins + 1
				pos[1][0] = self.x+1
				pos[1][1] = self.y
		if self.e == 'a' and self.board[self.x][self.y-1] == 'C':
				self.board[self.x][self.y-1] = 'P'
				self.board[self.x][self.y] = '.'
				coins = coins + 1
				pos[1][0] = self.x
				pos[1][1] = self.y-1
		if self.e == 'd' and self.board[self.x][self.y+1] == 'C':
				self.board[self.x][self.y+1] = 'P'
				self.board[self.x][self.y] = '.'
				coins = coins + 1
				pos[1][0] = self.x
				pos[1][1] = self.y+1
	
	# Checking for position of the Wall
	def checkWall(self):
		global state
		if self.e == 'w' and self.board[self.x-1][self.y] == 'X':
			self.board[self.x][self.y] = 'P'
			state = 1
		if self.e == 's'and self.board[self.x+1][self.y] == 'X':
			self.board[self.x][self.y] = 'P'
			self.state = 1
			state = 1
		if self.e == 'a' and self.board[self.x][self.y-1] == 'X':
			self.board[self.x][self.y] = 'P'
			self.state = 1
			state = 1
		if self.e == 'd' and self.board[self.x][self.y+1] == 'X':
			self.board[self.x][self.y] = 'P'
			self.state = 1
			state = 1

class Ghost(person):
	
	def __init__(self, x, y, board, c):
		self.x = x
		self.y = y
		self.c = c
		self.board = board
	
	def position(self):
		place = 1
		while place != 2:
			a = randint(1, 4)
			# a = 1 is for s
			if a == 1 and self.board[self.x+1][self.y] == '.':
				self.board[self.x][self.y] = '.'
				if self.x+1 > 14 and self.board[0][self.y] == '.':
					self.board[0][self.y] = 'G'
				else:	
					self.board[self.x+1][self.y] = 'G'
				place = 2
				pos[self.c][0] = self.x+1
				pos[self.c][1] = self.y
				break
			# a = 2 is for w	
			if a == 2 and self.board[self.x-1][self.y] == '.':
				self.board[self.x][self.y] = '.'
				if self.x-1 < 0 and self.board[14][self.y] == '.':
					self.board[14][self.y] = 'G'
				else:
					self.board[self.x-1][self.y] = 'G'
				place = 2
				pos[self.c][0] = self.x-1
				pos[self.c][1] = self.y
				break
			# a = 3 is for d	
			if a == 3 and self.board[self.x][self.y+1] == '.':
				self.board[self.x][self.y] = '.'
				if self.y+1 > 34 and self.board[self.x][0] == '.':
					self.board[self.x][0] = 'G'
				else:	
					self.board[self.x][self.y+1] = 'G'
				place = 2
				pos[self.c][0] = self.x
				pos[self.c][1] = self.y+1
				break
			# a = 4 is for a	
			if a == 4 and self.board[self.x][self.y-1] == '.':
				self.board[self.x][self.y] = '.'
				if self.y-1 < 0 and self.board[self.x][34] == '.':
					self.board[self.x][34] = 'G'
				else:	
					self.board[self.x][self.y-1] = 'G'
				place = 2
				pos[self.c][0] = self.x
				pos[self.c][1] = self.y-1
				break

pos = []
pos = create_game() 
coins = 0
state = 0
state1 = 0
intro = 1

while(1):
	level = 1
	if intro == 1:
		print 'GAME BEGINS..!!!'
		print 'd -> move right'
		print 'a -> move left'
		print 'w -> move up'
		print 's -> move down'
		intro = 2
	print '\n'.join([''.join(row) for row in pos[2]])
	e = raw_input("Enter Move: ")
	person1 = person(e)
	pacman1 = pacman(pos[1][0], pos[1][1], e, pos[2])
	print "Score:",
	print coins
	pacman1.checkPlace()
	pacman1.checkWall()
	pacman1.checkGhost()
	pacman1.collectCoins()
	ghost1 = Ghost(pos[0][0], pos[0][1], pos[2], 0)
	ghost1.position()
	ghost2 = Ghost(pos[3][0], pos[3][1], pos[2], 3)
	ghost2.position()
	ghost3 = Ghost(pos[4][0], pos[4][1], pos[2], 4)
	ghost3.position() 
	if (state == 1 or state1 == 1 or e == 'q' ):
		print 'GAME IS OVER..!!'
		break	
	if coins == 30:
	 	level = level + 1
	 	print 'YOU WON THE GAME... :)'
		print 'NOW YOU ARE IN LEVEL ' + str(level)
		pos = create_game()
		intro = 1
