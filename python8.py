import os
from gtts import gTTS
from shutil import which

flag=0
command=input("Enter the command:")

check=open("command.txt","r")
if(command in check.read()):
 flag=1
 from gtts import gTTS
 tts = gTTS("Don't use same command Twice")
 tts.save('hello.mp3')
 os.system("mpg321 hello.mp3")

if(flag==0):
 if(which(command)):
  print("Success")
  os.system(command)






saved_command=open("command.txt","a")
saved_command.write(command)
saved_command.close()

