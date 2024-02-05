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
if len(s)!=0:	
	print(s)
else:
	print("Empty String")


# Using Stack::

# def reduce_string(s):
#     stack = []
    
#     for char in s:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
    
#     result = ''.join(stack)
    
#     if not result:
#         return "Empty String"
#     else:
#         return result

# # Test cases
# input_str_1 = "aabbccdd"
# output_1 = reduce_string(input_str_1)
# print(f"Input: {input_str_1}, Output: {output_1}")

# input_str_2 = "abba"
# output_2 = reduce_string(input_str_2)
# print(f"Input: {input_str_2}, Output: {output_2}")



