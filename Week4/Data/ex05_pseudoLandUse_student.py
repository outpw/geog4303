#******************************
# Class05Demo: Exercise 05 student prototype
# Created by:  Stefan Leyk
# Created on:  02/17/2014
# Updated on:  02/16/2020
#******************************
# Description: Exercise 05 prototype for students
# Shows a few solutions for different questions
# different solutions are possible of course
#*********************************************************
#*****Function-based Solution*****************************
#*********************************************************
def readFIle(myPar):
    print "Running readFIle()"

def splitContents(myPar):
    print "Running splitContents()"

def calcToUrbanChange(myPar1,myPar2):
    print "Running calcToUrbanChange()"

txtFile = "Y:\\PATH TO TXT FILE"

#Call the functions you defined above...

#*********************************************************
#*****Procedural Solution*********************************
#*********************************************************
lc1988 = []
lc1999 = []
lc2009 = []

lcChange = []

#***Example: Procedural analysis of "NO CHANGE" locations**********
for myIndex in range(0,len(lc1988)):
    if lc1988[myIndex] == lc1999[myIndex] and lc1999[myIndex] == lc2009[myIndex]:
        lcChange.append(1)
    else:
        lcChange.append(0)
        
print "There are "+str(sum(lcChange))+" locations that did not change."



