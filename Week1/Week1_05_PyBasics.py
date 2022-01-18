'''*********************************************
Authors: G. Maclaurin, St. Leyk & A. Stum
Date: 12/11/2012 (last mod. 01/2020)
Purpose: Introduction to python in 100 lines
*********************************************'''
#Declaring variables: #variables are declared with a single equal sign
#numbers
a = 3
b = 4
c = 1.5
#characters (referred to as strings) are enclosed in quotes
#single (') and double (") quotes are treated the same
d = 'hello'
e = " world"
#a space is also a character, as well as numbers
f = '123'
#this is a string, not a number
cc = str(c)
#you can convert between data types
ff = int(f)
aa = float(a)
#int() is for integer, str() is for string, float() is for ... guess
dd = int(d)
#convert only if logically possible: you can't convert letters to numbers,
#but you can convert numbers to characters (i.e. a string object)
#booleans:
#boolean is a datatype, and an important one; take this simple example:
g = 3
a==g
#the double equal sign tests if the two objects are equal
#this is a logical operator, it tests a condition
b==g
#more logical operators that return a boolean
a>g
a<=g
#concatenation:
cat1 = d+e
cat2 = d+e+str(c)
#you must convert numbers to a string before concatenation
#lists:
l1 = [1,2,3]
#this is a list, simply it is a collection of objects
l2 = ['a','b','c']
#lists can contain numbers or strings (or any other data type)
l3 = ['abcd',1,'2',3.4,'3d']
#or a combination of different data types
l1[0]
#this returns the first element of the list
#you can access the elements of a list by what is called indexing
#indexing in python always starts at 0
l1[1]
#this returns the second element of the list, from now on
#lets call this index 1 rather than element 2, to avoid
#confusion
#You can use the range function to create a sequenced list
r1 = range(5)
#this is just an easy way of creating a list
#the range function starts at 0 if only one parameter is given, and it creates
#a sequenced list up to BUT NOT including that number.
r2 = range(1,5)
#if you give two parameters, the first is the starting number and the second is
#the stopping number, BUT it counts up to but not including the stop number
l4 = []
#this is an empty list
l4.append(1)
#this is one way of populating the list
#the print function:
print a
#or
print(a)
print d+e+str(c)
#looping:
#there are two kinds of loops: for and while
k = 'abcdef'
for i in k:
    print i
#this is a fundamental structure in programming
#you can read this as "For each element in k, print that element."
#you will learn about the 'in' operator in the full lab0, we use it
#with interation using a for loop
#for and in establish the structure of the for loop
#i is what we call the iterable. You can call it anything you want, i is just
#a convention. But don't use names that already exist in python
#k is an iterable object. An iterable object is one that is a collection of
#objects, such as lists or strings. Numbers are not iterable
for elem in l3:
    print elem
for i in range(len(l3)):
    print 'index:'
    print i
    print 'value'
    print l3[i]
#Think about how these two examples are different. What is the iterable in each?
#This seems like a simple difference, but it's powerful in application.
#How about a more complicated example
myList = []
for char in d:
    myList.append(char)
myList
#this splits the string d into a list