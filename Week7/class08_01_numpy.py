#******************************
# Class08_01Demo: Numpy Demo for Classes 07 & 08
# Created by:  Stefan Leyk
# Created on:  03/03/2014
# Updated on:  03/08/2020
#******************************
# Description:  
## Purpose: Testing local map algebra functionality of Numpy
## Sources: Very procedural but nice to learn some basics about overlays in grids
## and the use of Numeric functions and objects
#******************************
##import chgWorkDir2GDAL_t
##reload(chgWorkDir2GDAL_t)

import numpy

#***************************************************************************
#Just creating an array and play with it...*********************************
myA1 = numpy.array(([4,6,4,7,2],[5,8,4,9,7],[6,8,3,4,2],[9,5,8,6,7],[5,2,7,9,1],[7,4,2,6,7]))
mySubArray = myA1[2:4][1:3]
print "Array 1: The array looks like this:\n", myA1
print "Indexing Array 1:", myA1[2,3], myA1[2][3]
print "Clipping to a subregion is easy:\n", mySubArray
print "Slicing through row nr three only provides:", myA1[2,:]
print "Slicing through col nr three only provides:", myA1[:,2]
print "The shape of the array 1 is:", myA1.shape
numpy.size(myA1)
numpy.size(myA1,1)
numpy.size(myA1,0)

#***************************************************************************
#Applying the where function plus comparison functions to create a new grid*
print myA1
myA2 = numpy.where(numpy.greater(myA1,4),1,0)
print "Array 2: Values greater than 4=1, all others = 0:\n", myA2
myA2a = numpy.where(numpy.equal(myA1,4),1,0)
print "Array 2: Values greater than 4=1, all others = 0:\n", myA2a

#***************************************************************************
#Adding values of two arrays by using .add ufunc****************************
myA3 = numpy.add(myA1,myA2)
print "Array 3: Adding these two arrays equals:\n", myA3

#***************************************************************************
#******Adding element-wise two grids by counted looping*********************
myA4 = numpy.zeros(myA1.shape)
print "Array 4: Empty array:\n", myA4

for i in range (0,numpy.size(myA1,1)):
    for j in range (0,numpy.size(myA1,0)):
        myA4[j][i] = myA1[j][i] * myA2[j][i] + 100

print "Array 4: Adding up array 1 and array 2:\n", myA4

#******Alternative: Matrix functions .add() and .multiply()*****************     
myA4a = numpy.add(numpy.multiply(myA1, myA2),100)
print "Array 4: Adding up array 1 and array 2:\n", myA4a        


#***************************************************************************
#******Find values between 4 and 6 (mark with 1 and all others with 0)******
myA1 = numpy.array(([4,6,4,7,2],[5,8,4,9,7],[6,8,3,4,2],[9,5,8,6,7],[5,2,7,9,1],[7,4,2,6,7]))
#type of "shape"?
myA1.shape
myA_Range = numpy.zeros(myA1.shape).astype(int)

for i in range (0,numpy.size(myA1,1)):
    for j in range (0,numpy.size(myA1,0)):
        if myA1[j][i] >= 4 and myA1[j][i] <= 6:
            myA_Range[j][i] = 1
        else:
            myA_Range[j][i] = 0

print "myArrayRange"
print myA_Range                

#******Alternative: Matrix functions****************************************         
print "arrGreater4"
myA_GreatEqu4 = numpy.where(numpy.greater_equal(myA1,4),1,0)
print myA_GreatEqu4

print "arrLess6"
myA_LessEqu6 = numpy.where(numpy.less_equal(myA1,6),1,0)
print myA_LessEqu6

print "product:"
print myA_GreatEqu4 * myA_LessEqu6

#******Second alternative: in one step**************************************
myA_Range_a = numpy.multiply(numpy.where(numpy.less_equal(myA1,6),1,0),
               numpy.where(numpy.greater_equal(myA1,4),1,0))

print myA_Range_a
#***************************************************************************