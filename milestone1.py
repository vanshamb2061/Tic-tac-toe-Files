def display_board():	
	arr=[1,2,3],[4,5,6],[7,8,9]
	i=0
	j=0
	while i<3:
		print(f"{arr[i][0]} | {arr[i][1]} | {arr[i][2]} ")
		i+=1

def player_input(player1,player2):
	playerA='X'
	playerB='O'
	while (playerA=='X' or playerA='O') and (playerA=='X' or playerB=='O'):
		playerA=input("PLEASE ENTER YOUR SYMBOL (X/O) for Player A: ")
		playerB=input("PLEASE ENTER YOUR SYMBOL (X/O) for Player B: ")

def place_marker(player1,player2):
	ans=input("ENTER the position where you want to place your marker")
