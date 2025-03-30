# this program will allow a user to create new students and to view students.
# it will be large so I will break it up into smaller bits
# Author : Orla Woods

# first we have to define the functions we will need in the program
def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View Students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip() # removes any #leading and trailing 
#whitespace (spaces, tabs, newline characters, etc.) from a string
    return choice

# test the function
# choice = displayMenu() 
# print(f"you chose { choice }")

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name(blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        # Not doing error handling
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        #now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

        return modules

def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{ module['grade']}")
        
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# main program
students = []
choice = displayMenu()
while (choice != 'q'):
    # we could do this with lambda functions but keeping simple for now
    if choice == 'a':
        doAdd(students)
    if choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice=displayMenu()
          




    
