n = int(input())
graph = [[] for i in range(n)]

for current_page in range(n):
    pages = list(map(int, input().split()))
    graph[current_page] += pages[1::]

for row in range(len(graph)):
	graph[row] = len(graph[row])

graph = [row for row in graph if row != 0]

if max(graph) == 0:
	print('N')
	print(0)

else:
	print('Y')
	print(min(graph))

