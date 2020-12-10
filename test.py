import random
L = 3
K = []
for i in range(L):
	current = chr(random.randrange(97, 97 + 26))
	K.append(current)
print(K)