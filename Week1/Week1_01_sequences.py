#*****************************************
# Class01Demo(1): Sample sequential Python code
# Filename:       Week1_01_sequences.py
# Created by:     Stefan Leyk
# Created on:     01/17/2017
# Updated on:     01/06/2022, PW
#-----------------------------------------
# Description:  A simple script to execute some commands in a sequence
#*****************************************

print "This is a story about 10 trees \
that thought they would all be one forest.\n"
countDeciduous = 0
countConiferous = 0
#------------------------------------
# Here are the single characters ...
#------------------------------------
firstTree = "Pine"
print "A ", firstTree, " has been recorded."
countConiferous = countConiferous + 1

secondTree = "Oak"
print "A ", secondTree, " has been recorded."
countDeciduous += 1 # a shortcut instead of the above method

thirdTree = "Spruce"
print "A ", thirdTree, " has been recorded."
countConiferous += 1
#...
#------------------------------------
# Summarizing tree counts
#------------------------------------
print "This forest contains ", countConiferous, " coniferous trees \
and ", countDeciduous, " deciduous trees."