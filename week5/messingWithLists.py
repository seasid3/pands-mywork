# Messing with lists
# The code examples are in the jupyter nb in course materials
#
# Author: Orla Woods

'''
boats =["Sigma", 23, [1,2,3], {}] # lists are heterogneous

boats = boats + [1,2,3] # adds [1,2,3] into the boats list

boats.append("blah") # appends "blah" to the END of the list

boats.sort() # sorts the list but wont work for a mix of strings and integers'

print(boats) # prints boats with the [1,2,3] list and "blah" at the end

# see https://docs.python.org/3/tutorial/datastructures.html for more list methods
# see the w3 schools tutorial'

'''

'''
boats = ["Sigma", 23, [1,2,3], {}] 

for boat in boats:
    print(type(boat))

'''

ages = [12, 21, 23, 34] # you cant sum if there is a string in there

sum = 0 # you have to assign where the sum function will start, in this case 0

for age in ages:
    sum += age # += means you add the age to the value before and this then revers to the new value of sum
    # e.g. x = 5, x += 3, print(x) output will be 8. x has become reassigned to 8 after 3 was added to 5
print(sum)





