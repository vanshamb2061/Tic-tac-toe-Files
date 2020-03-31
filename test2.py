arr=[1,2,3],[4,5,6],[7,8,9]
i=1
control=1
while i<10:
	if i%2==0:
		ans='O'
	else:
		ans='X'
	res=input(f"ENTER position for entering {ans}: ")
	print(res)
	print(ans)
	arr[0][0]='X'
	print(arr[0][0])

#	if res==1:
#		arr[0][0]=ans
#		print(arr[0][0])
#	elif res==2:
#		arr[0][1]=ans
#	elif res==3:
#		arr[0][2]=ans
#	elif res==4:
#		arr[1][0]=ans
#	elif res==5:
#		arr[1][1]=ans
#	elif res==6:
#		arr[1][2]=ans
#	elif res==7:
#		arr[2][0]=ans
#	elif res==8:
#		arr[2][1]=ans
#	elif res==9:
#		arr[2][2]=ans
#	print(arr)
#	i+=1