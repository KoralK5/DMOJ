N, H = input(), input()

ind, lst = 0, []
while True:
	if ind+len(N) > len(H):
		break
	elif ''.join(sorted(H[ind:ind+len(N)])) == ''.join(sorted(N)) and H[ind:ind+len(N)] not in lst:
		lst += [H[ind:ind+len(N)]]

	ind += 1

print(len(lst))

'''
aab
abacabaa
'''