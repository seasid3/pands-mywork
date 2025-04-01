# this program allows me to complete the quiz in the lab
# author: Orla Woods

# the with statement will automatically close the file
# when it is finished with it

# QUESTION 1:
'''
with open("test-a.txt") as f:
    data = f.read()
    print(data)

# the old way of doing this is 
# f = open ("test1.text")
# data = f.read()
# print(data)
# f.close()

# quiz answer is there will be an error when this runs as test-a.txt does not exist:
# FileNotFoundError: [Errno 2] No such file or directory: 'test-a.txt''

'''



'''
with open("test-b.txt", "w") as f:
    data = f.write("test b\n") #returns the number of chars written
    print(data)

with open("test-b.txt", "w") as f2: #open file again
    data  =f2.write("another line\n")
    print (data)

# quiz answer. the number of characters per function is the output
# 7
# 13

# the contents are the number of characters in f1 and f2'
'''

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") #returns the number of chars written
    print(data)

with open("test-d.txt", "a") as f2: #open file again
    data  = f2.write("another line\n")
    print (data)

    # quiz answer is same as before