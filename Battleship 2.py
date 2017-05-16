from random import randint
import colorama
from colorama import Fore, Back, Style

board = []
ships = []
ready = False
while ready == False:
	print
	board_size = int(input('What size do you want your board??'))
	n_try = int(input('How much try do you want??'))
	n_ships = int(input('How much ship do you want??'))	
	
	if board_size >= 5 and n_ships <= board_size:
		ready = True
	if board_size < 5:
		print ('Board too Small!')
	if n_ships > board_size:
		print ('Too much ship for the Board size!')
	

for x in range(board_size):
	board.append(["O"] * board_size)

def print_board(board):
	for row in board:
		print (" ".join(row))

    

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)

def ship_built(ship_size, b_size):
	#print
	#print('ship size', ship_size)
	ship_ok = False
	while ship_ok == False:
		ship_list = []
		s_s_row = randint(0, b_size)
		s_s_col = randint(0, b_size)
		ship_list.append([s_s_col, s_s_row])
		direction = randint(0, 3)
		#print('Direction', direction)
		for x in range(ship_size -1 ):
			if direction == 0:
				s_s_col -= 1 
				ship_list.append([s_s_col, s_s_row])
			elif direction == 1:
				s_s_row += 1
				ship_list.append([s_s_col, s_s_row])
			elif direction == 2:
				s_s_col += 1
				ship_list.append([s_s_col, s_s_row])
			elif direction == 3:
				s_s_row -= 1
				ship_list.append([s_s_col, s_s_row])    
		#print ('Ship List 1', ship_list)
		for point in ship_list:
			if (point[0] >= 0 and point[0] <= b_size) and (point[1] >= 0 and point[1] <= b_size):
				ship_ok = True
				#print ('Point OK', point)
			else:
				ship_ok = False
				#print('Point Rejeter', point)
	
	#print ('Ship List 2', ship_list)
	return ship_list
	
def game_over(board, ships):
	for ship in ships:
		for point in ship:
			board[point[0]][point[1]] = 'S'
	print_board(board)
	print
	print ('GAME OVER')
	
def detail_ship(ships):
	print ('Ship detail')
	sh = 1
	for ship in ships:
		print ('Ship no', sh, 'is', len(ship), 'spaces long,')
		sh += 1
	print
	
	

	
## Create all the Ship.


ships.append(ship_built(randint(2, 5), board_size - 1))	
print ('Ship', ships)

for x in range(n_ships - 1):
	ship_separate = False
	while ship_separate == False:
		ship_separate = True
		ship_test = ship_built(randint(2, 5), board_size - 1)
		for ship in ships:
			for pts in ship :
				for t in ship_test:
					if pts == t:
						ship_separate = False
						#print('New ship overlap other one!')
	print('Ship', ship_test)
	ships.append(ship_test)

#print ('SHIPS', ships)
detail_ship(ships)


print ("Let's play Battleship!")
ship

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(n_try):
	
	hit_list = []
	hit = True
	print
	print ('It is turn:', turn + 1, 'of ', n_try)
	while hit == True:
		print_board(board)
		hit = False
		row = int(input("Guess Row: "))- 1
		col = int(input("Guess Col: "))- 1
		guess = [row, col]
		
		if guess[0] < 0 or guess[0] > board_size - 1 or guess[1] < 0 or guess[1] > board_size - 1:
			print ("Oops, that's not even in the ocean.")
		elif board[guess[0]][guess[1]] == "X" or board[guess[0]][guess[1]] == "H" :
			print ("You guessed that one already.")
		else:
			for ship in ships:
				if board[guess[0]][guess[1]] == 'H':
					break
				for pts in ship:
					if pts == guess:
						hit = True
						print(Fore.RED +'You hit a battleship')
						board[guess[0]][guess[1]] = 'H'
						hit_list.append(guess)
						break
					else:
						board[guess[0]][guess[1]] = 'X'
			if board[guess[0]][guess[1]] == 'X':
				print ("You missed the battleship!")
				
		
		if hit_list != []:
		
			for ht in hit_list:
				for ship in ships:
					if ht in ship:
						ship.remove(ht)
			des_ship = []
			for s in range(len(ships)):
				if ships[s] == []:
					print ("Congratulations! You sunk one battleship!")
					des_ship.append(s)
			for ds in des_ship:
				ships.remove(ships[ds])
	
		if ships == []:
			hit = False
			print
			print  ("Congratulations! You sunk all the Fleet. ")
			print
			break
		

game_over(board, ships)	
	
#if guess_row == ship_row and guess_col == ship_col:
#    print ("Congratulations! You sunk one battleship!")
#   break
#else:
#    if (guess_row < 0 or guess_row > b_size - 1) or (guess_col < 0 or guess_col > b_size - 1):
#		  print ("Oops, that's not even in the ocean.")
#	   elif(board[guess_row][guess_col] == "X"):
#		  print ("You guessed that one already.")
#	   else:
#		  print ("You missed my battleship!")
#		  board[guess_row][guess_col] = "X"
#		  
#	   if turn == 3:
#		  print ('Game Over')
#		  
#			
#	# Print (turn + 1) here!
#	print ('Turn', turn + 1)
#	board[ship_col][ship_row] = 'S'
#	print_board(board)
#	print ('Ship located at: ', ship_col, ship_row)
#
