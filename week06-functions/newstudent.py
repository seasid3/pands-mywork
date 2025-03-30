# this program prepares the student code for us in studentsWeek06.py
#Author: Orla Woods

students = []
def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

# test
doAdd(students)

doAdd(students)
print(students)

# modules

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
    
