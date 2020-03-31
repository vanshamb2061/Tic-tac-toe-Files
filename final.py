def display_board(arr):	
	a=0
	while a<3:
		print(f"{arr[a][0]} | {arr[a][1]} | {arr[a][2]} ")
		a+=1

def win_check(arr):
	i=0
	while i<3: #to check horizontal
		if arr[i][0]==arr[i][1] and arr[i][1]==arr[i][2]:
			print(f"Row {i+1} of {arr[i][0]} formed.")
			return 0
		i+=1
	j=0
	while j<3:
		if arr[0][j]==arr[1][j] and arr[1][j]==arr[2][j]:
			print(f"Column {j} of {arr[0][j]} formed.")
			return 0
		j+=1
	if arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2]:
		print(f"Primary Diagonal formed of {arr[0][0]}.")
		return 0
	elif arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0]:
		print(f"Secondary Diagonal formed of {arr[1][1]}.")
		return 0
	else:
		return 1

def place_marker(arr):
	i=1
	control=1
	while i<=9 and control==1:
		if i%2==0:
			ans='O'
		else:
			ans='X'
		import os
		res=int(input(f"ENTER position for entering {ans}: "))
		os.system("cls") # Windows
		if res==1:
			arr[0][0]=ans
		elif res==2:
			arr[0][1]=ans
		elif res==3:
			arr[0][2]=ans
		elif res==4:
			arr[1][0]=ans
		elif res==5:
			arr[1][1]=ans
		elif res==6:
			arr[1][2]=ans
		elif res==7:
			arr[2][0]=ans
		elif res==8:
			arr[2][1]=ans
		elif res==9:
			arr[2][2]=ans
		display_board(arr)
		control=win_check(arr)
		if control==0:
			i-=1
			if i%2==0:
				return 'O'
			else:
				return 'X'		
		print(f"Control = {control}, Iteration : {i}")
		i+=1

arr=[1,2,3],[4,5,6],[7,8,9]
a=0
print('\n'*100)
while a<3:
	print(f"{arr[a][0]} | {arr[a][1]} | {arr[a][2]} ")
	a+=1	#displaying grid in form of numpad
player1='X'
player2='O'
player1=input("PLAYER 1: Do you want to be X or O: ")
if player1=='X':
	player2=='O'
	print("Player 1 will go first")
else:
	player2=='X'
	print("Player 2 will go first")
winner=place_marker(arr)
if winner==player1:
	print("THE WINNER OF THE GAME IS PLAYER1")
else:
	print("THE WINNER OF THE GAME IS PLAYER2")