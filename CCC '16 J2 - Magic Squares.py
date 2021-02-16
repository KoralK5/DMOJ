inp = input().split('\n')
for row in range(len(inp)):
	inp[row] = [int(a) for a in inp[row].split(' ')]

mx, sums = max([len(row) for row in inp]), []
for row in range(len(inp)):
	while len(inp[row]) != mx:
		inp[row].append(0)

mag = 'magic'
if len(set([sum(row) for row in inp])):
	mag = 'not magic'

sms = []
for row in range(mx):
	sms += [sum([x[row] for x in inp])]

if len(set(sms)) > 1:
	mag = 'not magic'

print(mag)
