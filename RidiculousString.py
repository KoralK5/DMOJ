def check(S, T):
	num = -1
	for row in T:
		if row in S:
			S = S[S.find(row):]
		else:
			return 0
	return 1
	
input()
S, T = input(), input()
brk = 1
for elem in T:
	if elem not in S:
		brk = 0
		print(-1)
		break

num = 0
newS = S
while brk:
	if check(newS, T):
		print(len(newS))
		break
	else:
		newS += S[num]
	num = (num+1)%len(S)
