"""
# ---------------------------
# File           : q2.py
# Created        : 30-09-2021 09:45
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Count the numbers of even & odd numbers in the series of numbers
"""
if __name__ == "__main__":
   oddcount = 0
   evencount = 0
for val in range(1, 10):
    if val % 2 == 0:
        evencount = evencount+1
    else:
        oddcount = oddcount+1

print("Odd number count {} and even number count {}".format(oddcount, evencount))