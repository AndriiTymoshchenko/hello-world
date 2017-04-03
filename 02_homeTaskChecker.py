# -*- coding: utf-8 -*-
"""
Hometask "if-elif-else"

Created on Thu Mar 30 11:39:50 2017

@author: Andrii
"""

homeTasksCompleted = input("\n\nInput quantity of completed script exercises for 2017-04-01: ")

if homeTasksCompleted >= 3:
    print("\nWell done!")
elif homeTasksCompleted >= 1:
    print("\nKeep work, it's should be important for YOU!")
else:
    print("\nDone it, NOW!")
