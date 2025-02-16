# lab3.2.4extra.py
# This program completes the extra task for lab 3.2
# Author Orla Woods 

import math
numbertoconverttocent = float(input("Please enter an amount: "))
centamount = abs(numbertoconverttocent) * 100
print("The amount in cent is {}".format(int(centamount)))
# I used copilot here to find out how I make sure there is no decimal .0 in
# the final output as the abs value gave cent.0. I used int to remove the decimal