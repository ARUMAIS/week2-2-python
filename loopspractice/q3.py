"""
# ---------------------------
# File           : q3.py
# Created        : 30-09-2021 22:14
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Accept the string from the user
# Calculate the no.of.uppercase,lowercase & digits in that string
"""
if __name__ == "__main__":
    stringline = input("Enter the string that includes combination of numbers, uppercase & lowercase:")
    upper = 0
    lower = 0
    digit = 0
    for m in stringline:
       if m.isupper():
        upper += 1
       elif m.islower():
        lower += 1
       elif m.isdigit():
        digit += 1
       else:
            print("pass")
    print("The above string contains {} uppercase letters, {} lowercase letters,{} digits.".format(upper, lower, digit))

