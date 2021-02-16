'''P, N, R = int(input()), [int(input())], int(input())

while sum(N) <= P:
	N += [N[-1]*R]
	
print(len(N)-1)
'''

from math import log
P, N, R = int(input()), int(input()), int(input())

if R != 1:
	print(int(log(P, R)))
else:
	print(int(P/N))
