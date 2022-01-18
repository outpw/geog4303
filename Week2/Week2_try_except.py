#******************************
# Class03_02_Demo: Principles of try: and except:
# Created by:  Stefan Leyk
# Created on:  01/24/2016
# Updated on:  01/07/2022, PW
#******************************
# Description:  Demo to better understand the purpose of
# try: and except blocks in your Python code
# Caution: Built-in errors ...;-)
#******************************

import traceback
import sys

try:
    print "Starting my analysis"
    a = 34
    b = "45"
    g = a + b
    print "The result is:", g

except:
    print "Woops! You messed up!"
    # below uses the traceback module
    tb = sys.exc_info()[2]
    print tb
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    print pymsg
    
    
#for field in fields:
#    print (str(field.name))
