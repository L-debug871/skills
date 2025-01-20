#Lerato Moholo
#08/08/2024
#Write a program to calculate volume if sphere from radius

r = eval(input("Enter the radius of the sphere: \n" ))
from math import *
v = (4/3)* pi  * r**3
rounded_num = "{:.2f}".format(v)
if r<0:
    print("The radius must not be negative.")
else:
    print(f"The volume is {rounded_num}.")