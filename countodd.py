count = 0
question = 0
while question < 10:
    number= int(input("Enter an integer value:\n"))
    question += 1
    rem = number%2
    
    if rem !=0: # number is odd
        count=count+1


if count == 0 :
    print("There are 0 odd numbers.")
elif count ==1 :
    print("There is 1 odd number.")
elif count>1:
    print(f"There are {count} odd numbers.")
    