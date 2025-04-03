# this programe stores a student name and a list of her courses and grades in a dict, and then will print
# out her data and will keep going until there is a blank module name
# Author: Orla Woods

'''

student = {
    "name" : "Mary",
    "modules" : [
        {
        "courseName":"Programming",
        "grade" : 45
       },
       {
        "courseName":"History",
        "grade" : 99
       }
    ]
         }


print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))'
    '''

# empty list to store all students' data

students = []

# loop to handle multiple students

while True:
    # initialise an empty student dictionary for each student
    student = {
        "name" : "",
        "modules" : []
    }

    # PART A: Read in the student's name:
    student["name"] = input("Enter student's name: ")

    # sanity check: print ("Student: {}".format(student["name"])) this worked

    # PART B: read in the module names until the user enters a blank module name
    while True:
        # read the module name
        module_name = input("Enter the next module name (leave blank to quit): ")

        # stop if the module name is left blank:
        if module_name == "":
            break

        # sanity check print(module_name)

        # Part C: read in the grade for that module
        grade = int(input(f"Enter the grade for {module_name}: "))

        # append the module and its grade to the modules list
        student["modules"].append({"courseName": module_name, "grade": grade})

    # Add the student dictionary to the students list
    students.append(student)

    # ask if the user wants to add another student
    another_student = input("Do you want to add another student?(Yes/No): ").strip().lower()
    if another_student != "yes":
        break

# Part D: print all students' name and their module details

for student in students:
    print(f"\nStudent: {student['name']}")
    for module in student["modules"]:
        print (f"\t{module['courseName']}\t: {module['grade']}")

