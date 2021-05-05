import os
import jackson.reverse_tcp
import dustin, jackson, maria, matthew, russel 

#-------------PLEASE READ-------------#
#Please put everything your project needs to function in your respective folder
#If you need multiple folders please create it in your respective folders
#When installing packages using the terminal please make sure you have navigated to your folder before installing
#If you install into the SE-Semester-4-Proj folder your program wont be able to find it and wont work
#Try to make your project start using one python file so that the menu can run it via the users input
    #If this isnt possible just let me know. We can probably figure something out

progList = []
folderList = ['matthew', 'jackson', 'maria', 'russel', 'dustin']
#files = os.listdir('matthew') + os.listdir('jackson') + os.listdir('maria') + os.listdir('russel') + os.listdir('dustin')

for i in folderList:
    files = os.listdir(i)
    for f in files:
        if '.py' in f:
            progList.append(i + ' : ' + f)

def mainMenu():
    print("\nWelcome to the Indiana Tech Pen Testing Toolkit or the IT-PTT for short!")
    print("Type --h for a list of commands and how to use them")
    while True:
        strChoice = input("\n"+"IT-PTT>> ")
        if strChoice == "--h":
            menuHelp()
        elif strChoice == "--l":
            listPrograms()
            break
        elif strChoice == "--e":
            return
        else:
            print("Invalid command. --help for list of commands")

def menuHelp():
    print("\n"+"--help")
    print("--l Lists all programs")
    print("--i Select which program to use, ex: --i 1")
    print("--e Exit")

def listPrograms():
    i = 1
    for f in progList:   
        print(str(i) + ': ' + f)
        i = i + 1
    print(str(i) + ': ' + 'main menu')
    print('\nEnter a number:')
    strChoice = input('\nIT-PTT>> ')
    if (strChoice == '4'):
        mainMenu()
    else:
        runProgram(strChoice)

def runProgram(choice):
    for index, value in enumerate(progList):
        if int(choice) - 1 == index:            
            parts = value.split(' : ')
            print('starting ' + parts[0] + "'s " + parts[1] + '...')
            os.system('py ' + parts[0] + '/'+ parts[1])

#Start
mainMenu()