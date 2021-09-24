import os
import tkinter

def endprogram():
    os.system("taskkill/im cmd.exe /f")
# in front of the /IM, enter the name of the program/file you want to end

btn = tkinter.Button(padx = 25, pady=25, text= "Click me", command =endprogram)
btn.pack(padx = 100, pady=50)
#creates the button gui

# all this is, is a program that creates a button that closes something, its almost useless because task manager exists but oh well





