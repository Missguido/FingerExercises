# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:00:22 2019

@author: baysi
"""

counter = 1 
largest_odd = 0
even_count = 0
while counter <= 10:
    x = int(input("Enter an integer: "))
    if (x % 2 != 0 and x > largest_odd) or (x % 2 != 0 and x <= 0 and largest_odd == 0):
        largest_odd = x
        #print(largest_odd, " is the largest odd number so far")
    elif x % 2 == 0:
        even_count = even_count + 1
        #print(x , " is an even number", " even count: ", even_count)
    counter = counter + 1
if even_count == 10:
    print("No odd numbers were input")
else:
    print(largest_odd, " is the largest odd number so far")