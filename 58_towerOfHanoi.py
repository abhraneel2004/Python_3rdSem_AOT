
def towerofHanoi(n,from_, to , aux):
	if n==0:
		print("---")
		return
	if n==1:
		print(from_,'--->',to)
		return
	else:
		towerofHanoi(n-1, from_ , aux, to)
		print(from_,'--->',to)
		towerofHanoi(n-1, aux, to, from_)

a = int(input("Enter the number of disk: "))
towerofHanoi(a, "A", "B", "C")
