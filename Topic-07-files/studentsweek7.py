# this program uses the program we made last week, and creates a new menu item called save.
# Author: Orla Woods

import json
# the array we store everything in 
students= []
FILENAME="students.json"
def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty array
    # we can do this later
    with open(FILENAME) as f:
        return json.load(f)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(l) Load students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q):").strip() 

    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules
def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}" )
def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
def doSave():
    writeDict(students)
    print("students saved")
def doLoad():
    # we are changing the global variable students 
    # so we need to indicate this
    # (this stumped me for a little bit)
    global students 
    students = readDict()
    print ("students loaded")

# main program

choice = displayMenu()
while (choice != 'q'):
    # we could do this with lambda functions but keeping simple for now
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == "s":
        doSave()
    elif choice == 'l':
        doLoad()
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice=displayMenu()
          

