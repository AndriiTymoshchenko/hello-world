# -*- coding: utf-8 -*-
"""
Even number checker (two alternate "if" implementations)

Created on Thu Mar 30 10:27:54 2017

@author: Andrii
"""
print("\n\nCheking number for evenity\n")

number=input("Input number: ")


# alternate 1
state = "\nOops, this number is odd!" if number%2 else "\nNumber is even, relax man :)"
print(state)

# alternate 2
numberEvenity = not bool(number%2)

verify = numberEvenity and "\nI'm sure, checked twice" or "\nTry to add 1 to it."
print(verify)
