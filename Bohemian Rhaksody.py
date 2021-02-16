# inp = [row.split(' ') for row in input().split('\n')]
# H, W  = inp[0][0], inp[0][1]

'''H, W = 4, 4
stage = []
for row in range(H):
	stage += [[[] for _ in range(W)]]
'''

x, y=0, 0
for row in range(len(inp)):
	x += inp[row][0]; y += inp[row][1]
x /= len(inp); y /= len(inp)

