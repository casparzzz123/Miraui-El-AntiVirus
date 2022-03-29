import os
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()


try:
        Tk().withdraw()
        filename = askopenfilename()
        print(filename)
        with open(filename) as file:
            found = 0
            damage = 0  
            for line in file:
                words = line.split()
                for word in words:
                ## checks for virus
                    if word == "VIRUS":
                        found = found + 1
                        print("found a virus") 
                ## checks for notepad virus
                    if word == "notepad":
                        found = found + 1
                        print("found a virus")
                ## checks for Deletion Virus
                    if word == "DEL":
                        found = found + 1
                        print("found a virus")
                ## checks for shutdown virus
                    if word == "shutdown":
                        found = found + 1
                        print("found a virus")
                ## checks for msg box virus
                    if word == "msg":
                        found = found + 1
                        print("found a virus")
                ## checks for windows register virus
                    if word == "reg":
                        found = found + 1
                        damage = damage + 1
                        print("found a SERVERLY VIRUS")
                

        print("You Have " + str(found) + " Viruses!")
        print("You Have " + str(damage) + " SEVERLY VIRUSES!")      

        print("PRESS ENTER TO EXIT")
        input("e")
        print("Bye!")
except FileNotFoundError:
        print("Error: No Files Found?")

    
