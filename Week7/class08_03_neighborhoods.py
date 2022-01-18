#******************************
# Week07_03:  Numpy Demo for Week 7 on neighborhoods
# Created by:  Stefan Leyk
# Created on:  03/03/2014
# Updated on:  1/11/2022, PW
#******************************
# Description:  
# Purpose: Understand how filters and other neighborhood functions work
# Convolutions & Slicing techniques
# Remember, 1 is horizontal axis (rows), 0 is vertical axis (columns)
# ******************************
import numpy
# ****************************************************************************
# Just creating an array and play with it...*********************************
#myArray1 = numpy.array(([4,6,4,7,2],[5,8,4,9,7],[6,8,3,4,2],[9,5,8,6,7],[5,2,7,9,1],[7,4,2,6,7]))
myArray1 = numpy.array(([4,6,4,7,2,7],[5,8,4,9,7,4],[6,8,3,4,2,2],[9,5,8,6,7,6],[5,2,7,9,1,7]))
print myArray1
print myArray1.max()

# ***************************************************************************
# *************Neighborhood analysis: Min filter*****************************
#BREAK DOWN WHAT'S GOING ON HERE IN CONSOLE... 
myArray2 = numpy.zeros(myArray1.shape).astype(float)
for i in range (1,numpy.size(myArray1,1)-1):
    for j in range (1,numpy.size(myArray1,0)-1):
        myMin = myArray1.max()
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):
                if myArray1[jj][ii]<myMin:
                    print myArray1[jj][ii]
                    myMin=myArray1[jj][ii]
        myArray2[j][i] = myMin
print "Array 2: That easy is writing a min filter:\n", myArray2


# **************Slicing Variant*****************************
myArray2a = numpy.zeros(myArray1.shape).astype(float)
for i in range (1,numpy.size(myArray1,1)-1):
    for j in range (1,numpy.size(myArray1,0)-1):
        #print myArray1[j][i]
        #print myArray1[j-1:j+2,i-1:i+2]
        #print myArray1[j-1:j+2,i-1:i+2].min()
        myArray2a[j][i] = myArray1[j-1:j+2,i-1:i+2].min()
        
print "Array 2a: That easy is writing a min filter:\n", myArray2a


# ***************************************************************************
# **************Neighborhood analysis: Focal Sum*****************************
myArray3 = numpy.zeros(myArray1.shape).astype(float)
for i in range (1,numpy.size(myArray1,1)-1):
    for j in range (1,numpy.size(myArray1,0)-1):
        sum = 0.0
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):
                sum = sum + myArray1[jj][ii]
        myArray3[j][i] = sum
        
print "Array 3: That easy is writing a focal sum function:\n", myArray3

# **************Slicing Variant*****************************
myArray3a = numpy.zeros(myArray1.shape).astype(float)
for i in range (1,numpy.size(myArray1,1)-1):
    for j in range (1,numpy.size(myArray1,0)-1):
        myArray3a[j][i] = myArray1[j-1:j+2,i-1:i+2].sum()

print "Array 3a: That easy is writing a focal sum function:\n", myArray3a
# ***************************************************************************