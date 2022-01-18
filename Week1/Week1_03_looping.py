#*****************************************
# Class01Demo(3): Build a forest through iteration
# Filename:       Week1_03_iteration.py
# Created by:     Stefan Leyk
# Created on:     01/17/2017
# Updated on:     01/06/2022, PW
#-----------------------------------------
# Description:  Forest demo based on 
# principles of branching (if-elif-else statements)
# in a counted loop (iteration) and in a while loop
#*****************************************

countDeciduous = 0
countConiferous = 0
#------------------------------------
# Here are the single characters ...
#------------------------------------
myTrees = ["Pine","Oak","Pine","Oak"]

# a counted loop example

for tree in myTrees:
    print tree
    
    '''
    if tree == "Pine":
        print "A ", tree, " - a coniferous tree - has been recorded."
        countConiferous += 1
        
    elif tree == "Oak":
        print "A ", tree, " - a deciduous tree - has been recorded."
        countDeciduous += 1
        
    else:
        print "No idea what tree this is."
    '''

    
'''
# a while loop example
countTrees = 0

while countTrees<len(myTrees):
    tree = myTrees[countTrees]
    print tree
    
    if tree == "Pine":
        print "A ", tree, " - a coniferous tree - has been recorded."
        countConiferous += 1
    elif tree == "Oak":
        print "A ", tree, " - a deciduous tree - has been recorded."
        countDeciduous += 1
    else:
        print "No idea what tree this is."
        
    countTrees+=1

#------------------------------------
# Summarizing tree counts
#------------------------------------
print "This forest contains ", countConiferous, " coniferous trees \
and ", countDeciduous, " deciduous trees."
#------------------------------------
# Our forest...
#------------------------------------
if countConiferous > countDeciduous:
    print "Seems this is a coniferous forest."
elif countConiferous < countDeciduous:
    print "Seems this is a deciduous forest."
else:
    print "Seems this is a mixed forest."

#------------------------------------
'''