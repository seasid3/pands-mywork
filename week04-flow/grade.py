# grade.py
# This program reads a student's grade, checks it is valid and 
# prints out the grade
# Author: Orla Woods

percentage = float(input("Enter the percentage: "))

# make sure the number is valid (between 0 and 100) 

while percentage < 0 or percentage > 100:
     percentage = float(input("Please enter a number between 0 and 100:"))

# round the percentage to the nearest whole number

roundedpercentage = round(percentage) or round(newnumber)

# print the rounded percentage

print (f"Percentage for grading is {roundedpercentage}")

# grading based on rounded percentage

if roundedpercentage < 40: 
     print ("Fail")

elif roundedpercentage < 50:
     print ("Pass")

elif roundedpercentage < 60:
     print ("Merit 2")

elif roundedpercentage < 70:
     print ("Merit 1")

else: print ("Distinction")
             
#End