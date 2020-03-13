import datetime 

timenow=datetime.datetime.now()
houronly=timenow.hour

if(houronly in range(12,15)):
	print('Good Afternoon')
elif(houronly in range(15,19)):
	print('Good Evening')
elif(houronly in range(19,24)):
	print("Good night")
elif(houronly in range(3,11)):
	print('Good morning')
elif(houronly in range(0,3)):
	print("Good night")




