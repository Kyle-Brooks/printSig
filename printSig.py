#File: printSig.py
#Author: Sathenus
#Date Modified: 3/19/2017
import time
def printSig():
    name = "Sathenus"
    print("Author: " + "%s" % (name))
    print("Date & Time Modified: " + time.strftime("%c"))

printSig()
