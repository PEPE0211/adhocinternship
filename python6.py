#For Creating A file
new_file=open("check.txt","w")
new_file.write('This is just to check if progrram works or not....')
	

#For Reading file
new_file = open("check.txt", "r")
print(new_file.read())


#for copyin files from check to check2

file_name = input('Enter a New File to copy contents or an old file to overwrite::')
second_file = open(file_name,"w")
second_file.write(new_file.read())
print(second_file)
second_file.close()

#FOr appending files


firstfile = input('Enter the file to be append from:')
file1=open(firstfile,"r")
secondfile = input('Enter the file to be append to:')
file2 = open(secondfile,"a")
file2.write(file1.read())
file1.close()
file2.close()




