"""
booleans are true or false functions
they are represented by the bool() function
bool is called a boolean constructor
"""

#the value of zero is considered to be false
print("0 is : {}".format(bool(0)))

#any whole number is considered to be true
print("1 is : {}". format(bool(1)))

#floats are true
print("5.4 is : {}". format(bool(5.4)))

#empty strings are false
print("empty string is : {}". format(bool("")))

#normal strings are true
print("normal string is : {}". format(bool("food")))

#creating an empty variable without defining the type
a = None