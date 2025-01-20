# Purpose: Generate a personalised spam message based on the user's details
# Author:  Moholo Lerato
# Date: 02/08/2024

first_name = input("Enter first name:" "\n")
last_name  = input("Enter last name:" "\n")
money =  int(input("Enter sum of money in USD:" "\n"))
Country =input("Enter country name:" "\n")
money30 = float(money*3/10) 
ammount= str(money)+ "USD"  #to move from 1234 USD to 1234USD
ammount_30=str(money30)+ "USD" #to move from 370 USD to 370USD
print("") # the spam message:
print("Dearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,", sep="\n")
print(f"General Fayk {last_name}, your long lost relative from Mapsfostol.", sep="\n")
print(f"My father left the sum of {ammount} for us, your distant cousins.", sep="\n")
print(f"Unfortunately, we cannot access the money as it is in a bank in {Country}.", sep="\n")
print("I desperately need your assistance to access this money.", sep="\n")
print(f"I will even pay you generously, 30% of the amount - {ammount_30},", sep="\n")
print("for your help.  Please get in touch with me at this email address asap.", sep="\n")
print("Yours sincerely", sep="\n")
print(f"Frank {last_name}")