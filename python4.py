import os
import crypt

user_name = input('Enter Your username:')
Check=[1,2,3,4,5,6,7,8,9,0]
f=0
for i in user_name:
	if i in str(Check):
		f=1
	


if(f==0):
 password='hello'+user_name
 encpass=crypt.crypt(password,'22')
 os.system('useradd -p '+ encpass +user_name)
 print('user created')
else:
 	print('You entered an integer value in the username')

