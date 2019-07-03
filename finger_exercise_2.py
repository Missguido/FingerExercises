# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:28:50 2019

@author: M Guido

"""
# Write a program that examines three variables - x, y, and z and prints the largest odd number among them.
# If none of them are odd, it should print a message to that affect.


x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))
 
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:    # Check if all numbers are even
    print('None of the x, y, z are odd!')
     
elif y < x and z < x: 
    if x % 2 != 0:    # Check if x is the biggest and odd
        print('x is the largest odd number!')
    else:     
        if y < z and z % 2 != 0:    # Compare y and z and see which one's odd
            print('z is the largest odd number!')
        elif z < y and y % 2 != 0:
            print('y is the largest odd number!')
        else:    # Used else because if both y and z were even, if statement above would've got it
            print('y and z, both are the largest odd numbers!')
 
 
elif x < y and z < y:
    if y % 2 != 0:
        print('y is the largest odd number!')
    else: 
        if x < z and z % 2 != 0:
            print('z is the largest odd number!')
        elif z < x and x % 2 != 0:
            print('x is the largest odd number!')
        else:
            print('x and z, both are the largest odd numbers!')
         
elif x < z and y < z:
    if z % 2 != 0:
        print('z is the largest odd number!')
    else: 
        if y < x and x % 2 != 0:
            print('x is the largest odd number!')
        elif x < y and x % 2 != 0:
            print('y is the largest odd number!')
        else:
            print('y and z, both are the largest odd numbers!')
         
else:    # If none of the conditionals are true, they're all the same and odd
    print('all numbers are the same odd numbers!')