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

def readFile(txtFile):
    with open(txtFile,'r') as data:
        dataLines = data.readlines()
    return dataLines

def splitContents(dataLines):
    lineList = []
    i = 0
    while i < len(dataLines):
        lineList.append(dataLines[i].split(','))
        i += 1
    return lineList
    
    
def calcToUrbanChange(line0,line1,line2):
    outList = []
    for i in range(0,len(line0)):

        if line2[i] == '4' and (line0[i] != '4' or line1[i] !='4'):
            outList.append(1)
    
        else:
            outList.append(0)
    return outList
    
def urbanPortion(lcData):
    urbanCount = 0
    for x in lcData:
        if x == '4':
            urbanCount += 1
    return (float(urbanCount)/float(len(lcData)))*100
            
txtFile = "C:\Users\phwh9568\GEOG_4303\Week4\Data\class05exercise.txt"

#Call the functions you defined above...

data = readFile(txtFile)

lc1989 = splitContents(data)[0]
lc1999 = splitContents(data)[1]
lc2009 = splitContents(data)[2]

lcChange = calcToUrbanChange(lc1989,lc1999,lc2009)
urban2009portion = urbanPortion(lc2009)

print lcChange
print urban2009portion


#*********************************************************
#*****Procedural Solution*********************************
#*********************************************************

''' 

lcChange = []

with open(txtFile,'r') as data:
    lc1989 = data.readline().split(',')
    lc1999 = data.readline().split(',')
    lc2009 = data.readline().split(',')


for i in range(0,len(lc1989)):

    if lc2009[i] == '4' and (lc1989[i] != '4' or lc1999[i] !='4'):
        lcChange.append(1)

    else:
        lcChange.append(0)

urban2009count = 0
for x in lc2009:
    if x == '4':
        urban2009count += 1

urban2009portion = (float(urban2009count)/float(len(lc2009)))*100

print lcChange
print urban2009portion


#***Example: Procedural analysis of "NO CHANGE" locations**********
    

for myIndex in range(0,len(lc1988)):
    
    if lc1988[myIndex] == lc1999[myIndex] and lc1999[myIndex] == lc2009[myIndex]:
        lcChange.append(1)
    else:
        lcChange.append(0)
        
print "There are "+str(sum(lcChange))+" locations that did not change."
'''


