N = int(input())

def origin(P, C):
	return 100*P/(C+100)

for row in range(N):
	P, C = [float(row) for row in input().split(' ')]
	print(origin(P, C))
