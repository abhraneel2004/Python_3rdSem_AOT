s = input("Enter a string: ")
s = [k for k in s]
c = True
while c:
	count = 0
	for i in range(len(s)-1):
		if (s[i]==s[i+1] and s[i]!='@'):
			s[i] = '@'
			s[i+1] = '@'
			count+=1
			
	s = ''.join(s)
	s = s.replace('@','')
	s = [k for k in s]
	if count==0:
		c = False
		break
		
s = "".join(s)
print(s)
