# More messing with functions
# flexible arguments
# Author: Orla Woods

# print(1, 2, 3, sep="", end="\t") # t is a tab
# print("hi")

# function take 

#def fun1(*args): #unnamed argument
#    print(type(args))
#    for val in argsL
#        print(val)

# fun1("a", "b", "c")

# keyword arguments
# def fun2(**kwargs): # keyword args
#    print(type(kwargs))
#    print(kwargs)
    # for val in args:
    #     print(val)   

# fun2(name = "joe", age = 21, gender = "M")

#when would you use this:

# sample code. a prog to take the average. in real life there is a fucntion to get a sum in tuples so
# you wouldnt do this,it's just an example

def ave(*values): # the code here is not related to the code outside the "black box of the function". see &&
    number_of_values =  len(values)
    sum = 0
    for value in values:
        sum+=value

    average = sum/ number_of_values
    return average, sum # this returns a tuple (average, sum)

#print(ave(1,2,3,4,5,6))

av1, sum_of_numbers = ave(1,2,3,4,5,6) #&& see the indent above, the values on this line are not related to 
# the indented code above, ie the "black box of the function". forget about what you put in the black box and
# continue with the code here. see here on rhs of equals you use the ave function on 1-6, so it is actually
# finding the average and sum above in the black box return line BUT i have no given them av1 and sum_of_numbers
# as variable names. but python is actually returning the return value of the ave function in a tuple ie 
# (average, sum). python puts av1 as the first value in the tuple and sum_of_numbers as the second

print(f"{av1} and sum is {sum_of_numbers}")