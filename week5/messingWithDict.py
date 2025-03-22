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

'''

car = {
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner" : {
        "name" : "Andrew",
        "drive-numer" : 1123
    }
    }

print(car["owner"]["name"])'
'''

car = {
    "make" : "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags" : ["pre-owned", "best buy", "Dealer"],
}

#print (car)

# to prinit out the keys (ie make, model, price, tags)

#for key in car:
#    print(key, " has value ", car[key])

# neater to use the items:
#  comma puts a space in between the key and value

for key, value in car.items():
    print(key, "has a value", value)




