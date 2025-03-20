# grade.py
# This program reads a student's grade, checks it is valid and 
# prints out the grade
# Author: Orla Woods

percentage = float(input("Enter the percentage: "))
print (f"percentage is {percentage}")

if percentage < 0 or percentage > 100:
     print ("Please enter a number between 0 and 100")

elif percentage < 40:
     print ("Fail")

elif percentage < 50:
     print ("Pass")

elif percentage < 60:
     print ("Merit 2")

elif percentage < 70:
     print ("Merit 1")

else: print ("Distinction")
             
#End