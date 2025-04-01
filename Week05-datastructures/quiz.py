# this just gives the code in the quiz and the answers
# author: Orla Woods

numberOfQuestions = 5
averageAge = 23.4
debugMode  = True
name = "joe"
ages = []
months = ("Jan", "Feb", "Mar")
book = {}
stuff = [ 12, "Fred", False, {}]
someone = dict(firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching" : [{ 
        "courseName" : "programming", 
        "semester" : 1
        }, {
        "courseName" : "Data Representation", 
        "semester" : 2
        }
        ]
}

print(me["teaching"][0]["semester"])

print(me["teaching"][0]["courseName"])


# a. What is the type of the variable numberOfQuestions? int
# b. What is the type of the variable averageAge? float
# c. What is the type of the variable debugMode? boolean
# d. What is the type of the variable name? string
# e. What is the type of the variable ages? list
# f. What is the type of the variable months? tuple
# g. What is the tyoe of the viable in months[1]? string of value "Feb"
# h. What is the type of the variable book? dict
# i. What is the type of the variable stuff? list
# j. what is the type of variable in stuff[2]? bool of value False
# k. what is the type of the variable someone? dict
# l. what is the type of the variable someone["firstname"]? variable with the string value of Joe. when you
# access the key "firstname" you're actually retrieving the vlaue associated with the key, i.e., "Joe"
# m" what is the type of the variable me? dict
# n. what is the type of the variable me["teaching"]? list. the actual word teaching is a key
# o. what is the type of the variable me["teaching"][0]["semester"]? 1 which is a int
# p. trick question: what is the type of the variable me["teaching"][0]["coursename"]? string called programming WRONG
# the code has a capital N in courseName so the answer is undefined for variable type

#  
