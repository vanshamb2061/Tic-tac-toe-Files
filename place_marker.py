def place_marker(arr):
	i=1
	control=1
	var=0
	while i<=9 and control==1:
		if i%2==0
			ans='O'
			flag=2
		else:
			ans='X'
			flag=1
		res=input(f"ENTER position for entering {flag}")
		if res==1:
			arr[0][0]=ans
		elif res==2:
			arr[0][1]==ans
		elif res==3:
			arr[0][2]==ans
		elif res==4:
			arr[1][0]==ans
		elif res==5:
			arr[1][1]==ans
		elif res==6:
			arr[1][2]==ans
		elif res==7:
			arr[2][0]==ans
		elif res==8:
			arr[2][1]==ans
		elif res==9:
			arr[2][2]==ans
		display_board(arr)
		i+=1
		control=win_check(arr)
		if control==0:
			i-=1
			if i%2==0:
				return 'O'
			else:
				return 'X'