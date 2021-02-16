inp = int(input())

for row in range(inp):
	n = int(input()) 
	i = n//4
	j = [192, 442, 692, 942]

	if n-i*4 == 0: 
		print(int(str(i-1) + str(j[n-i*4-1]))) 
	else: 
		print(int(str(i) + str(j[n-i*4-1])))