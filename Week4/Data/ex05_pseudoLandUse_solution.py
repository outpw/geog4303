#******************************
# Class0Demo: Exercise 05 solution examples
# Created by:  Stefan Leyk
# Created on:  02/17/2014
# Updated on:  02/21/2020
#******************************
# Description: Shows a few possible solutions
# for exercise class05; different solutions are 
# possible of course; see a few different options below
#******************************

def readFIle(txtFile):
    print "Running readFIle()"
    if os.path.isfile(txtFile) == True:
        txtF = open(txtFile,'r')
        myFileContents= txtF.readlines()
        txtF.close()
        return myFileContents

def splitContents(myFileContents):
    print "Running splitContents()"
    i = 0
    lcIntListObj = []
    while i<len(myFileContents):
        lcStrList = myFileContents[i].split(',')
        lcIntList = [int(j) for j in lcStrList]
        lcIntListObj.append(lcIntList) 
        i += 1
    return lcIntListObj
#----------------------------------------
def calcToUrbanChangeLong(a,b,c):
    print "Running calcToUrbanChangeLong()"
    lcChange = []
    for i in range(0,len(a)):
        if a[i] != b[i] and b[i] == 4 or b[i] != c[i] and c[i] == 4:
            lcChange.append(1)
        else:
            lcChange.append(0)
                
    print "There are "+str(sum(lcChange))+" locations that changed to urban (class 4)."
    return sum(lcChange)

def calcToUrbanChangeListCompr(a,b,c):
    print "Running calcToUrbanChangeListCompr() - Solution using list comprehension"
    lcChange = [1 if a[i] != b[i] and b[i] == 4 or b[i] != c[i] and c[i] == 4 else 0 
                for i in range(0,len(a))]
    print "There are "+str(sum(lcChange))+" locations that changed to urban (class 4)."
    return sum(lcChange)

def calcToUrbanPix(a,b,c):
    print "Running calcToUrbanPix()"
    if a != b and b == 4 or b != c and c == 4:
        return True
    else:
        return False

def calcToUrbanPixDirectAssg(a,b,c):
    print "Running calcToUrbanPixDirectAssg()"
    return a != b and b == 4 or b != c and c == 4
        
#def calcToUrbanPix2(a,b,c):
#    print "Running calcToUrbanPix2()"
#    if a[i] != b[i] and b[i] == 4 or b[i] != c[i] and c[i] == 4:
#        return True
#    else:
#        return False

#******************************************
import os,sys
txtFile = r"C:\Users\phwh9568\GEOG_4303\Week4\Data\class05exercise.txt"

myFileContents = readFIle(txtFile)
myIntLCListObject = splitContents(myFileContents)

lc1988 = myIntLCListObject[0]
lc1999 = myIntLCListObject[1]
lc2009 = myIntLCListObject[2]


#*************************************
#1) Run the whole iteration in an external function, (explicit for loop)
toUrbChg = calcToUrbanChangeLong(lc1988,lc1999,lc2009)
print "There are ", str(toUrbChg), " places that changed to urban. "
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)

#*************************************
#2) Run the whole iteration in an external function as list comprehension
toUrbChg = calcToUrbanChangeListCompr(lc1988,lc1999,lc2009)
print "There are ", str(toUrbChg), " places that changed to urban. " 
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)

#*************************************
#3) Call the function for each iteration - explicit for loop
toUrbChg=[]
for i in range(len(lc1988)):
    if calcToUrbanPix(lc1988[i],lc1999[i],lc2009[i])==True:
        toUrbChg.append(1)
    else:
        toUrbChg.append(0)
print "There are ", toUrbChg.count(True), " places that changed to urban are: ", str(toUrbChg)
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)

#*************************************
#4) Call the function for each iteration - explicit for loop
# and direct assignment with return value from fct.
toUrbChg=[]
for i in range(len(lc1988)):
        toUrbChg.append(calcToUrbanPixDirectAssg(lc1988[i],lc1999[i],lc2009[i]))
print "There are ", toUrbChg.count(True), " places that changed to urban are: ", str(toUrbChg)
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)

#*************************************
#5) Call the function for each iteration - embedded in a list comprehension    
toUrbChg=[]
toUrbChg = [1 if calcToUrbanPix(lc1988[i],lc1999[i],lc2009[i])==True else 0 
    for i in range(0,len(lc1988))]
print "There are ", toUrbChg.count(True), " places that changed to urban are: ", str(toUrbChg)
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)

#*************************************
#6) Call the function for each iteration - embedded in a list comprehension
#direct assignment in fct 
toUrbChg=[]
toUrbChg = [calcToUrbanPixDirectAssg(lc1988[i],lc1999[i],lc2009[i]) 
    for i in range(0,len(lc1988))]
print "There are ", toUrbChg.count(True), " places that changed to urban are: ", str(toUrbChg)
print "The proportion urban landuse in 2009 is: ",float(lc2009.count(4))/len(lc2009)


