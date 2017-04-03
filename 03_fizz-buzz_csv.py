# -*- coding: utf-8 -*-
"""
Fizz-Buzz game implementation on Python
with functions

Created on Thu Mar 30 09:31:22 2017

@author: Andrii
"""
import sys
import csv

# ==================== Input section ============================
print("\n\n\nIt's a Fizz-Buzz game. Use numbers from fb.txt.\n")

# ==================== Functions ================================
def fizzBuzz(fbg):
    '''
    fizzBuzz function takes list "fbg" and return Fizz-Buzz 
    string using first three elements from list
    '''
    answerFB = ''
    
    for i in range(1,fbg[2]+1):
           
        answer_i = str(i)
        
        if not i % fbg[0]:
            answer_i = 'F'
            
        if not i % fbg[1]:
            if answer_i=='F':
                answer_i += 'B' 
            else: answer_i = 'B'
        
            
        answerFB += answer_i + ' ' 
    return answerFB

# ==================== Code =====================================

# List for fizz-buzz sequences
fbSeq = []

# Read input data
with open(sys.argv[1], 'r') as data:
    reader = csv.reader(data, delimiter=' ')
    for row in reader:
        if len(row) < 3:
            pass
        else:
            for j in range(len(row)):
                row[j] = int(row[j])
            fbSeq += [row]

# Generate fizz-buzz sequences
fbAns = []
for row in fbSeq:
    fbAns += [fizzBuzz(row)]



# ==================== Output ===================================

for i in range(len(fbSeq)):
    print(fbSeq[i], " : ", fbAns[i],"\n")