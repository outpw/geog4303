#******************************
# Class07Demo: Numpy Demo for Class 07
# Created by:  Stefan Leyk
# Created on:  03/03/2014
# Updated on:  02/28/2020
#******************************
# Description:  
## Purpose: Testing functionality of Numpy
## Sources: Very procedural but nice to learn some basics about neighborhood analysis in grids
## and the use of Numeric functions and objects
#******************************
##import chgWorkDir2GDAL_t
##reload(chgWorkDir2GDAL_t)

import numpy
#***************************************************************************
#Just creating an array and play with it...*********************************
myArray1 = numpy.array(([4,6,4,7,2],[5,8,4,9,7],[6,8,3,4,2],[9,5,8,6,7],[5,2,7,9,1],[7,4,2,6,7]))
mySubArray = myArray1[2:4][1:3]
print "Array 1: The array looks like this:\n", myArray1
print "Indexing Array 1:", myArray1[2,3], myArray1[2][3]
print "Clipping to a subregion is easy:\n", mySubArray
print "Slicing through row nr three only provides:", myArray1[2,:]
print "Slicing through col nr three only provides:", myArray1[:,2]
print "The shape of the array 1 is:", myArray1.shape
numpy.size(myArray1)
numpy.size(myArray1,1)
numpy.size(myArray1,0)
#***************************************************************************
#Applying the where function plus comparison functions to create a new grid*
myArray1
myArray2 = numpy.where(numpy.greater(myArray1,4),1,0)
myArray2a = numpy.where(numpy.equal(myArray1,4),1,0)
print "Array 2: Values greater than 4=1, all others = 0:\n", myArray2
#***************************************************************************
#Adding values of two arrays by using .add ufunc****************************
myArray3 = numpy.add(myArray1,myArray2)
print "Array 3: Adding these two arrays equals:\n", myArray3
#***************************************************************************
#******Adding element-wise two grids by counted looping*********************
myArray4 = numpy.zeros(myArray1.shape)
print "Array 4: Empty array:\n", myArray4

for i in range (0,numpy.size(myArray1,1)):
    for j in range (0,numpy.size(myArray1,0)):
        myArray4[j][i] = myArray1[j][i] * myArray2[j][i] + 100
        
#******Alternative: Matrix functions .add() and .multiply()*****************     
myArray4a = numpy.add(numpy.multiply(myArray1, myArray2),100)
print "Array 4: Adding up array 1 and array 2:\n", myArray4        

#***************************************************************************
#******Find values between 4 and 6 (mark with 1 and all others with 0)******
myArray1 = numpy.array(([4,6,4,7,2],[5,8,4,9,7],[6,8,3,4,2],[9,5,8,6,7],[5,2,7,9,1],[7,4,2,6,7]))
#type of "shape"?
myArray1.shape
myArrayRange = numpy.zeros(myArray1.shape).astype(int)

for i in range (0,numpy.size(myArray1,1)):
    for j in range (0,numpy.size(myArray1,0)):
        if myArray1[j][i] >= 4 and myArray1[j][i] <= 6:                                         # and myArray5[j][i] != 0:
            myArrayRange[j][i] = 1
        else:
            myArrayRange[j][i] = 0

print "myArrayRange"
print myArrayRange                
#******Alternative: Matrix functions****************************************         
print "arrGreater4"
arrGreater4 = numpy.where(numpy.greater_equal(myArray1,4),1,0)
#print arrGreater4
print "arrLess6"
arrLess6 = numpy.where(numpy.less_equal(myArray1,6),1,0)
#print arrLess6
print "product:"
#print arrGreater4 * arrLess6

res = numpy.multiply(numpy.where(numpy.less_equal(myArray1,6),1,0),
               numpy.where(numpy.greater_equal(myArray1,4),1,0))

print res
#***************************************************************************