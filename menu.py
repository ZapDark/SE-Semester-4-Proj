import os
from pathlib import Path
import jackson.reverse_tcp

#-------------PLEASE READ-------------#
#Please put everything your project needs to function in your respective folder
#If you need multiple folders please create it in your respective folders
#When installing packages using the terminal please make sure you have navigated to your folder before installing
#If you install into the SE-Semester-4-Proj folder your program wont be able to find it and wont work
#Try to make your project start using one python file so that the menu can run it via the users input
    #If this isnt possible just let me know. We can probably figure something out

def mainMenu():
    print("Welcome to the Indiana Tech Pen Testing Toolkit or the IT-PTT for short!")
    print("Type --h for a list of commands and how to use them")
    while True:
        strChoice = input("\n"+"IT-PTT>> ")
        if strChoice == "--h":
            menuHelp()
        elif strChoice == "--l":
            listPrograms()
            break
        else:
            print("Invalid command. --help for list of commands")

def menuHelp():
    print("\n"+"--help")
    print("--l Lists all programs")
    print("--i Select which program to use, Ex. --i 1")

def listPrograms():
    p = Path(".")
    print(p.iterdir())
    if p.is_dir():
        print("True")
        #jackson.reverse_tcp.Hello()
    else:
        print("False")
    
    

mainMenu()