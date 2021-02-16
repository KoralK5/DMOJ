size = int(input())

data = []
for row in range(size):
	inp = input().split(' ')

	contain = inp[0]
	inside = inp[-1]

	done = False
	for row in range(len(data)):
		if data[row][0] == [contain]:
			data[row][1] += inside
			done = True
	
	if not done:
		data += [[[contain],[inside]]]

	print(data)

print(data)

for row in data:
	print(f'{row[0][0]} =','{'row[1][0]+ '}')



'''
9
A contains B
A contains c
B contains d
F contains A
F contains z
X contains Y
Y contains X
X contains x
Q contains R
'''