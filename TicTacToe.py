'''
Tic Tac Toe Game:
Conditional statements and loops used.
'''

# initialized the empty list as board.
lis01 = [" ", "|", " ", "|", " "]
lis02 = ["-", "-", "-", "-", "-"]
lis03 = [" ", "|", " ", "|", " "]
lis04 = ["-", "-", "-", "-", "-"]
lis05 = [" ", "|", " ", "|", " "]

# condition for strikes for 'O' and 'X'.
oStrik = ["O", "O", "O"]
xStrik = ["X", "X", "X"]

print("\n{0:*^66}\n\n".format(" TIC TAC TOE "))
flag = True
while flag:

	# player01's and player02's mark taken.
	player01 = input("Player one choose your mark ('O' or 'X'):").strip().upper()
	  
	if player01 == "O":
		player02 = "X"
		print("\nplayer01: '{}'\nplayer02: '{}'\n\n".format(player01, player02))
		flag = False

	elif player01 == "X":
		player02 = "O"
		print("\nplayer01: '{}'\nplayer02: '{}'\n\n".format(player01, player02))
		flag = False

	else:
		print("Invalid operator entered!\n\n")

# instructions printed.
print("Instructions:\nYou have to select the places by entering the numbers.")
print("Starting from top left to the bottom like this:\n")
print("{0:2}|{1:2}|{2:2}\n----------\n{3:2}|{4:2}|{5:2}\n----------\n{6:2}|{7:2}|{8:2}\n\n".format(0,2,4,6,8,10,12,14,16))

#for keeping the check on the outer loop
limit = 0

#for player selection. 
count = 1

# loop for not to exceed beyond 9.
while limit <10:

	# whenever value of count equals to 1, its player01 turn.
	while count == 1:
		playerOneInput = input("mark your place player01: ").strip()
		
		# check condition.
		if playerOneInput.isdigit() == False:
			print("Invalid input!")
		else:
			playerOneInput = int(playerOneInput)

			# if spot exists.
			if playerOneInput in (0,2,4,6,8,10,12,14,16):

				# if spot between 0 to 4 then update the lis01 list
				if playerOneInput >=0 and playerOneInput <=4:

					# if spot is already taken.
					if lis01[playerOneInput] == "X" or lis01[playerOneInput] == "O":
						print("Spot already marked!")
					else:

						# if spot is empty then update and display list as a board.
						lis01[playerOneInput] = player01
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01: 
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))

						# winning chances set in form of lists.
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]
						
						# all winning chances are grouped together. 
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]
						
						# if 'O' strik matches the winning lists.
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break
						
						# else if 'X' strik matches the winning lists.
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break

						# else if its a draw.
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0
						
						# else game not over yet then goes to player02.
						else:
							count = 2
				
				# if spot between 6 to 10 then update the lis03 list
				elif playerOneInput >=6 and playerOneInput <=10:
					
					# setting to lis03 actual index.
					playerOneInput -=6

					# checking if spot is empty.
					if lis03[playerOneInput] == "X" or lis03[playerOneInput] == "O":
						print("Spot already marked!")
					else:

						# if empty then displayed the updated list as a board.
						lis03[playerOneInput] = player01
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01:
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))

						# winning chances set in form of lists.
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]
						
						# all winning chances are grouped together. 
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]
						
						# if 'O' strik matches the winning lists.
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break
						
						# else if 'X' strik matches the winning lists.
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break

						# else if its a draw.
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0

						# else game not over yet then goes to player02.
						else:
							count = 2

				# if spot between 12 to 16 then update the lis05 list
				elif playerOneInput >=12 and playerOneInput <=16:

					# setting to lis05 actual index.
					playerOneInput -=12

					# checking if spot is empty.
					if lis05[playerOneInput] == "X" or lis05[playerOneInput] == "O":
						print("Spot already marked!")
					else:

						# if empty then displayed the updated list as a board.
						lis05[playerOneInput] = player01
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01:
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))
						
						# winning chances set in form of lists.
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]

						# all winning chances are grouped together.
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]

						# if 'O' strik matches the winning lists.
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break

						# else if 'X' strik matches the winning lists.
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break

						# else if its a draw.
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0

						# else game not over yet then goes to player02.
						else:
							count = 2
			
			# spot not on the board.
			else:
				print("Invalid spot!\n\n")

	'''
	if count = 2 then its player02 turn.
	Aproach for player02, is same as of player01.
	'''
	while count == 2:
		playerTwoInput = input("mark your place player02: ").strip()

		if playerTwoInput.isdigit() == False:
			print("Invalid input!")
		else:
			playerTwoInput = int(playerTwoInput)
			if playerTwoInput in (0,2,4,6,8,10,12,14,16):
				if playerTwoInput >=0 and playerTwoInput <=4:
					if lis01[playerTwoInput] == "X" or lis01[playerTwoInput] == "O":
						print("Spot already marked!")
					else:
						lis01[playerTwoInput] = player02
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01:
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))
						
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0
						else:
							count = 1
				
				elif playerTwoInput >=6 and playerTwoInput <=10:
					playerTwoInput -=6
					if lis03[playerTwoInput] == "X" or lis03[playerTwoInput] == "O":
						print("Spot already marked!")
					else:
						lis03[playerTwoInput] = player02
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01:
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))
						
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0
						else:
							count = 1

				elif playerTwoInput >=12 and playerTwoInput <=16:
					playerTwoInput -=12
					if lis05[playerTwoInput] == "X" or lis05[playerTwoInput] == "O":
						print("Spot already marked!")
					else:
						lis05[playerTwoInput] = player02
						lineOne = a = lineTwo = b = lineThree = ""
						for x in lis01:
							lineOne += x
						for x in lis02:
							a += x
						for x in lis03:
							lineTwo += x
						for x in lis04:
							b += x
						for x in lis05:
							lineThree += x
						print ("{}\n{}\n{}\n{}\n{}\n\n".format(lineOne, a, lineTwo, b, lineThree))
						
						win01 = [lineOne[0], lineTwo[0], lineThree[0]]
						win02 = [lineOne[2], lineTwo[2], lineThree[2]]
						win03 = [lineOne[4], lineTwo[4], lineThree[4]]
						win04 = [lineOne[0], lineTwo[2], lineThree[4]]
						win05 = [lineOne[4], lineTwo[2], lineThree[0]]
						win06 = [lineOne[0], lineOne[2], lineOne[4]]
						win07 = [lineTwo[0], lineTwo[2], lineTwo[4]]
						win08 = [lineThree[0], lineThree[2], lineThree[4]]
						win = [lineOne[::2], lineTwo[::2], lineThree[::2], win01, win02, win03, win04, win05, win06, win07, win08]
						if oStrik in win:
							print("'O' wins!\n\n")
							count = 0
							break
						elif xStrik in win:
							print("'X' wins!\n\n")
							count = 0
							break
						elif lineOne[::2].count(" ") == 0 and lineTwo[::2].count(" ") == 0 and lineThree[::2].count(" ") == 0:
							print("It's a Draw!\n\n")
							count = 0
						else:
							count = 1
			else:
				print("Invalid spot!\n\n")
	limit +=1