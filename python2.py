#write a code using  that will take user input from and search on google and store top 10 url in the list.


#conditions : 
 #   i )   URL must be stored permanently as well
#    ii)   user can give input using keyboard and  voice both

import webbrowser
from googlesearch import search
import speech_recognition as sr



def audioRec():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	 print("Your query")
	 audio = r.listen(source)
	file2write= open("url.txt","w")
	
	for i in search(r.recognize_google(audio),stop=10):
	 print(i)		       	
	 file2write.write(i+"\n")
	
	
	

def InputRec():
	query_input= input('Enter your query:')
	file2write= open("url.txt","w")
	for i in search(query_input,stop=10):
	 file2write.write(i+"\n")
	 print(i) 	
def switching(argument) :
    switcher={
        1:audioRec,
	2:InputRec
	}
    func= switcher.get(argument, lambda: "Invalid choice")
    return func()


argument=int(input("Enter YOur choice:\n1.VoiceInput\n2.textInput:"))
switching(argument) 
