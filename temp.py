# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:42:59 2017

@author: Andrii
"""

import sys

fbSeq = []

# Read input data
data = open("fb.txt","r")
lines = data.readlines()

for i in range(len(lines)):
    rowStr = lines[i]
    if i < (len(lines)-1):
        rowStr = rowStr[:-1]
    row=rowStr.split(" ")
    
rows=[]
        
for i in range(len(row)):
    for j in range(len(row[i])):
        rows[i][j] = int(row[i][j])
        print(row[i][j])