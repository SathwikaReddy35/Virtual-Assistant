import pyttsx3
import os
import gtts
from playsound import playsound
import speech_recognition as sr
def task1():
    with sr.Microphone(device_index=1) as source:
        print("Speak now!")
        converter.say("Sathwika, Speak Now")
        converter.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("Here is what I heard:")
            converter.say("Here is what I heard")
            converter.runAndWait()
            print(text)
            print("Enter the filename you want to create or that already exists to work on [PLEASE ADD THE .txt EXTENSION] : ")
            converter.say("Sathwika, Enter the filename you want to create or that already exists to work on. PLEASE ADD THE .txt EXTENSION")
            converter.runAndWait()
            filename1=input()
            with open(filename1,"a+") as my_file:
                print("This file already has the content as follows:\n")
                my_file.seek(0,0)
                if(my_file.read()!=''):
                    print(my_file.read())
                    print("\nAppending the content I heard.........\n")
                    converter.say("Sathwika, Appending the content I heard")
                    converter.runAndWait()
                #my_file.write(text)
                else:
                    ("New File Created")
                my_file.seek(0,0)
                print("Now,Your file has the following information:\n")
                converter.say("Sathwika, Now the files has the following information")
                converter.runAndWait()
                print(my_file.read())
                my_file.seek(0,0)
                mytext=my_file.read()
            my_file.close()
        except sr.UnknownValueError:
            print("It cannot be understood!! Sorry:(")
            converter.say("It cannot be understood!! Sorry")
            converter.runAndWait()
        except sr.RequestError:
            print("Results could not be found.")
            converter.say("Results could not be found.")
            converter.runAndWait()
            
    return
def task2():
    print("Enter the filename that already exists to work on [PLEASE ADD THE .txt EXTENSION] : ")
    converter.say("Sathwika, Enter the filename that already exists to work on. PLEASE ADD THE .txt EXTENSION")
    converter.runAndWait()
    filename1=input()
    with open(filename1,"a+") as my_file:
        my_file.seek(0,0)
        print("The file has the following information:\n")
        print(my_file.read())
        my_file.seek(0,0)
        mytext=my_file.read()
        myobj=gtts.gTTS(mytext)
        print("Enter the filename,the audio file has to be saved with [PLEASE ADD THE .mp3/mp4 EXTENSION] : ")
        converter.say("Enter the filename,the audio file has to be saved with . PLEASE ADD THE .mp3 or mp4 EXTENSION  ")
        converter.runAndWait()
        filename2=input()
        myobj.save(filename2)
        playsound(filename2)
    return 
def task3():
    print("Enter the filename you want me to read to you [PLEASE ADD THE .txt EXTENSION] : ")
    filename1=input()
    with open(filename1,"a+") as my_file:
        my_file.seek(0,0)
        print("NOW,The file has the following information:\n")
        print(my_file.read())
        my_file.seek(0,0)
        mytext=my_file.read()
        converter.say(mytext)
        converter.runAndWait()
        
    my_file.close()
    return
def task4():
    print("Enter the audio filename to play for you [WITH .mp3 EXTENSION] : ")
    converter.say("Enter the audio file to play for you . PLEASE ADD THE .mp3 or mp4 EXTENSION  ")
    converter.runAndWait()
    filename2=input()
    playsound(filename2)
    return


converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.8)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
converter.setProperty('voice', voice_id)

converter.say("Hello Sathwika, Iam your Voice Assistant. Call me Thaaara")
print("Hello Sathwika, Iam your Voice Assistant! Call me Tara :)")
converter.runAndWait()
print("Iam here to Read, Write and Revise Notes for you")
converter.say("Iam here to Read, Write and Revise Notes for you")
converter.runAndWait()
print("I can, \n1.Write notes/Append notes and save as Text file")
converter.say("I can,Write notes or Append notes and save as Text file")
converter.runAndWait()
print("2.Read a Text file for you and save as an Audio file")
converter.say("Read a Text file for you and save as an Audio file")
converter.runAndWait()
print("3.Read a Text file for you")
converter.say("Read a Text File for you")
converter.runAndWait()
print("4.Play an Audio file for you")
converter.say("Play an Audio file for you")
converter.runAndWait()
converter.say("So, Mentioned the list of tasks I can do for you")
converter.runAndWait()
link1="https://support.microsoft.com/en-us/windows/windows-speech-recognition-commands-9d25ef36-994d-f367-a81a-a326160128c7"
print("PLEASE REFER TO THIS BELOW LINK,FOR HOW TO SAY SPECIAL CHARACTERS IF NEEDED :)\n {}".format(link1))
converter.say("Sathwika, PLEASE REFER TO THIS LINK,FOR HOW TO SAY SPECIAL CHARACTERS if needed ")
converter.runAndWait()

flag1=1
input1=0
while(flag1==1) :
    flag2=0
    print("Would you like to perform some task now? Say Yes/No.") 
    converter.say("Would you like to perform some task now? If Yes, Say Yes Thaaara. else Say No.")  
    converter.runAndWait()


    r=sr.Recognizer()


    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            list_text=text.split()
            list_text= list(map(lambda x:x.lower(), list_text))
            print(list_text)
        except:
            print("Nothing heard! Sorry\nExited")
            converter.say("Nothing heard Sorry. Exited")
            converter.runAndWait()
            exit()

        if(("yes" in list_text) or ("yeah" in list_text) or ("yah" in list_text) and ("no" not in list_text) and ("dont" not in list_text) and ("not" not in list_text)):
            #flag1=1
            print('Sathwika, Please say your choice:')
            converter.say("Sathwika. Please say your choice ")
            converter.runAndWait()
            text=""
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                #print("text",text)
                list1=text.split(" ")
                list1= list(map(lambda x:x.lower(), list1))
                print("list1",list1)
            except:
                print("Nothing heard! Sorry.\nExited")
                converter.say("Nothing heard Sorry. Exited")
                converter.runAndWait()
                exit()
            if((flag2==0) and (('one' in list1) or ('first' in list1) or ('1' in list1)) and ("no"  not in list1) and ("not" not in list1) and ("dont" not in list1)  and ("second" not in list1) and ("third" not in list1) and ("fourth" not in list1)):
                input1=1
                converter.say("You choosed option")
                converter.say(input1)
                converter.say(" that is to write or append notes and save as text files")
                converter.runAndWait()
                flag2=1
            if((flag2==0) and (('two' in list1) or ('second' in list1) or ('2' in list1)) and ("no" not in list1) and ("dont" not in list1) and ("not" not in list1)):
                input1=2
                converter.say("You choosed option")
                converter.say(input1)
                converter.say("that is reading text files for you and saving them as audio files")
                converter.runAndWait()
                flag2=1
            if((flag2==0) and (('three' in list1) or ('third' in list1) or ('3' in list1)) and ("no" not in list1) and ("dont" not in list1) and ("not" not in list1)):
                input1=3
                converter.say("You choosed option")
                converter.say(input1)
                converter.say("that is reading a text file for you")
                converter.runAndWait()
                flag2=1
            if((flag2==0) and (('four' in list1) or ('fourth' in list1) or ('4' in list1)) and ("no" not in list1) and ("dont" not in list1) and ("not" not in list1)):
                input1=4
                converter.say("You choosed option")
                converter.say(input1)
                converter.say("that is playing an audio file for you")
                converter.runAndWait()
                flag2=1
            if(flag2==0):
                print("Nothing heard! Sorry\nExited")
                converter.say("Nothing heard Sorry..... Exited")
                converter.runAndWait()
                exit()
        elif("no" in list_text or "not" in list_text or "dont" not in list_text ):
            flag1=0
            converter.say("Exiting...Bye Sathwika, see you soon.")
            print("Bye Sathwika:)")
            converter.runAndWait()
            exit()
        else:
            print("Nothing heard Relevant.Exited")
            converter.say("Seems nothing heard relevant, Bye Sathwika")
            converter.runAndWait()
            exit()

        if(flag1==1 and flag2==1 and input1==1):
            task1()
        if(flag1==1 and flag2==1 and input1==2):
            task2()
        if(flag1==1 and flag2==1 and input1==3):
            task3()
        if(flag1==1 and flag2==1 and  input1==4):
            task4()
        
