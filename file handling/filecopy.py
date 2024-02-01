f1 = open("New.txt", "r") #opening parent file
x = input("Enter the file name to copy: ") #taking user input of new file/ exsiting file name
f2 = open(x+".txt", "w+") #"Opening that file"

data = f1.read() # reading data from first file
f1.close() # closing first file
f2.write(data) #writing the data to 2nd file

print("The data is copied") # Success message

f2.close()
