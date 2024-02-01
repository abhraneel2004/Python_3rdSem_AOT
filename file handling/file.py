#Writing data in a text file

with open("New.txt", "w+") as f:
	f.write("This is a new file created using python and i dont want to share this publicly. Today I was going to a place called hell.")
	#content can be anything
	
f.close()	
#file closing is necessary
