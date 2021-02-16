go = int(input())

for row in range(go):
	tri = [int(row) for row in input().split()]

	C = tri.pop(tri.index(max(tri)))

	if C**2 > tri[0]**2 + tri[1]**2:
		print('O')
	elif C**2 < tri[0]**2 + tri[1]**2:
		print('A')
	elif C**2 == tri[0]**2 + tri[1]**2:
		print('R')
