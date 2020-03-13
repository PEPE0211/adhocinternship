# Create a program that asks the user to enter their name and their age..Print out a message that will tell them the year that they will turn 95 years old.
from datetime import date
current_year=int(date.today().year)

user_name= input("Enter Your Name:")
user_age= int(input("Enter your Age:"))

age_difference=(95- user_age)
x=(current_year+age_difference)
if(user_age > 95):
	print(user_name+" You are already above 95")
elif(user_age < 95):
	print(user_name+" will turn 95 in  "+str(x))
elif(user_age == 95):
	print("YOu are 95 years old right now.")
	

