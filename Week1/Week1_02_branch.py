#*****************************************
# Class01Demo(2): First Branching Example
# Filename:       Week1_02_branch.py
# Created by:     Stefan Leyk
# Created on:     01/17/2017
# Updated on:     01/06/2022, PW
#-----------------------------------------
# Description:  Forest demo based on 
# principles of branching (if-elif-else statements)
#*****************************************

print "This is a story about 3 trees \
that thought they would all be one forest.\n"
countDeciduous = 0
countConiferous = 0
#------------------------------------
# Here are the single characters ...
#------------------------------------
firstTree = "Pine" #or 'Oak' 

if firstTree == "Pine":
    print "A ", firstTree, " - a coniferous tree - has been recorded."
    countConiferous+=1
    
elif firstTree == "Oak":
    print "A ", firstTree, " - a deciduous tree - has been recorded."
    countDeciduous+=1
    
else:
    print "An unknown species has been encountered."

#------------------------------------
# Summarizing tree counts
#------------------------------------
print "This forest contains ", countConiferous, " coniferous trees \
and ", countDeciduous, " deciduous trees."
#------------------------------------
# Our forest...
#------------------------------------
if countConiferous > countDeciduous:
    print "Could be a coniferous forest."
elif countConiferous < countDeciduous:
    print "Could be a deciduous forest."
else:
    print "Could be a mixed forest."

#------------------------------------