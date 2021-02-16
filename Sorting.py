inp = int(input())
ls = []

for row in range(inp):
	ls += [int(input())]

ls = sorted(ls)

for row in ls:
	print(row)

