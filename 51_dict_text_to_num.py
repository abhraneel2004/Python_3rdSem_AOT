
def text_to_num(s):
	if s.lower()=='zero':
		return 0
	if s.lower()=='one':
		return 1
	if s.lower()=='two':
		return 2
	if s.lower()=='three':
		return 3
	if s.lower()=='four':
		return 4
	if s.lower()=='five':
		return 5
	if s.lower()=='six':
		return 6
	if s.lower()=='seven':
		return 7
	if s.lower()=='eight':
		return 8
	if s.lower()=='nine':
		return 9
	

data_set = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}
max1 = text_to_num(data_set[list(data_set.keys())[0]])

for i in data_set.keys():
	if text_to_num(data_set[i])>max1:
		max1 = text_to_num(data_set[i])
		
print(max1)
