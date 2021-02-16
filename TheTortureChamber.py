n1, n2 = int(input()), int(input())

out1 = 0
sieve = [True] * (n1+1)
for p in range(2, n1+1):
	if (sieve[p]):
		out1 += 1
		for i in range(p, n1+1, p):
			sieve[i] = False

out2 = 0
sieve = [True] * (n2+1)
for p in range(2, n2+1):
	if (sieve[p]):
		out2 += 1
		for i in range(p, n2+1, p):
			sieve[i] = False

print(abs(out1-out2))