# Messing with dictionaries. 
# Author: Orla Woods.

'''

make = "ford"
model = "mondeo"
year = 2006
owner = "Andrew"'
'''


# but if i try to write for a second car (e.g. make2) this becomes very complicated
# so i can store in cars

# teherefore put in a dict object

car = {
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner" : {
        "name" : "Andrew",
        "drive-numer" : 1123
    }
    }

print(car["owner"]["name"])