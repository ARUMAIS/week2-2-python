"""
# ---------------------------
# File           : q1.py
# Created        : 30-09-2021 09:36
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# using break,continue & pass statements
# Create a loop with an if statement inside
# Add print statements in all stages
"""
actual_number = 10
while 1:
    print("GUESSING GAME")
    guess = int(input("Try to guess the number (1-10):"))
    if guess != actual_number:
        retry = input("Wrong guess, Do you want to try again, Enter N for No, Y for Yes")
        if retry == "N":
            break
        else:
            continue
    else:
        print("YES, you have guessed it.Its {}".format(actual_number))
        break
print("Thanks for playing")
print("END")