# messing with csv
# author Orla Woods

'''

import csv
FILENAME = "data.csv"
with open(FILENAME, "rt") as file:
    csvReader = csv.reader(file, delimiter = ',') # delimiter can be anything, in this case a comma
    for line in csvReader: # line will be a list containing the variables in each line
        age = line[2] # the age
        print(age) # note this is printing the header now, andrew provides a solution to this in the tutoral'
        '''

# creating a csv file and importing data

import csv

mydict = [{'first' : 'Andrew', 'last' : 'Beatty', 'age' : '22'},
          {'first' : 'Orla', 'last' : 'Woods', 'age' : '41'},
          {'first' : 'Banana', 'last' : 'Man', 'age' : '500'},
]

# field names
fields = ['first', 'last', 'age']

# name of csv file
FILENAME = "data2.csv"

#writing to csv file
with open(FILENAME, 'w', newline = '') as csvfile:
    #creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    #writing headers (field names)
    writer.writeheader()
    for dictrow in mydict:
        print(dictrow)
        writer.writerow(dictrow)