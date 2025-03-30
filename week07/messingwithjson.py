# messing with JSON
# This program demonstrates storing data is json format
# author: Orla Woods

import json

electricBill = {
    'name' : 'Orla',
    'amount' : '9999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f) # writes the dict object to the file as a JSON object

