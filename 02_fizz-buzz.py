# -*- coding: utf-8 -*-
"""
Fizz-Buzz game implementation on Python

Created on Thu Mar 30 09:31:22 2017

@author: Andrii
"""

# ==================== Input section ============================
print("\n\n\nIt's a Fizz-Buzz game. Please, insert three numbers.")

fizz = int(input("Fizz: "))
buzz = int(input("Buzz: "))
goal = int(input("Goal: "))

# ==================== Code =====================================

answerFB = ''

for i in range(1,goal+1):
       
    answer_i = str(i)
    
    if not i % fizz:
        answer_i = 'F'
        
    if not i % buzz:
        if answer_i=='F':
            answer_i += 'B' 
        else: answer_i = 'B'
    
        
    answerFB += answer_i + ' ' 

# ==================== Output ===================================

print(answerFB)

