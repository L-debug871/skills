# purpose: A program that calculates the area of a triangle from 3 given sides 
# author: Lerato Moholo
# date: 02/08/2024

#Ask for user input
a = float(input("Enter the length of the first side: " ))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Heron's formula
s=(a+b+c)/2
d = float((s*(s-a)*(s-b)*(s-c)))
if d>0:
    from math import *   # import math functions
    Area = round(sqrt(float(d)),2)
    print(f"The area of the triangle with sides of length {a} and {b} and {c} is {Area}.")
else:
    print("Error: The input does not describe a triangle.")