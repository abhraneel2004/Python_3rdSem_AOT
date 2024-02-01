
def isprime(n):
	if n==0 or n==1:
		return False
	f = 0
	for i in range(2, int(n**0.5)+1):
		if not n%i:
			f+=1
	return not f

def sumprime(n2):
	s = 0
	
	if isprime(n2) and n2>=2:
		for i in range(2,n2):
			if s==n2:
				return
			if isprime(i) and s<n2:
				print(i,"+")
				s+=i
		
a = int(input("enter the prime number: "))
sumprime(a)			
