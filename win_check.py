def win_check(arr):
	i=0
	while i<3: #to check horizontal
		if arr[i][0]==arr[i][1] and arr[i][1]==arr[i][2]:
			print(f"Row {i} of {arr[i][0]} formed.")
			return 0
		i+=1
	j=0
	while j<3:
		if arr[0][j]==arr[1][j] and arr[1][j]==arr[2][j]:
			print(f"Column {j} of {arr[0][j]} formed.")
			return 0
	if arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2]:
		print(f"Primary Diagonal formed of {arr[0][0]}.")
		return 0
	elif arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0]:
		print(f"Secondary Diagonal formed of {arr[1][1]}.")
		return 0
	else:
		return 1
	