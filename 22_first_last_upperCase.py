
s = input("Enter a string :")
words = s.split(' ')

for i in range(len(words)):
	alphas = [k for k in words[i]]

	alphas[0], alphas[-1] = alphas[0].upper(), alphas[-1].upper()

	words[i]= ''.join(alphas)

s = " ".join(words)
print(s)
