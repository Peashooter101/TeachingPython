"""
Variables and Data Types
----
Sometimes we might use the same values multiple times
or need to store a value to be edited later.

This is accomplished through the use of Variables.
"""
# There are a few standard *data types* in Python.
# They can all be stored and represented in variables.
# You declare a variable by giving it a name, then
# assigning its value using =.
# The values shown below after the = are known as *literals*.
# Literals mean "literally this value".

aBoolean = True     # Used to store a True / False (Yes or No) Value
aString = "String"  # Used to store text.
anInteger = 10      # Used to store whole numbers.
aFloat = 10.5       # Used to store numbers with fractional pieces.

# Variables in Python are *implicit*, meaning you do
# not specify the specific data type, it is *implied*
# by the value you assign to it.
#
# For example in Java (explicit), you will say `int myInt = 10;`
# However in Python (implicit), you will say `myInt = 10`
#
# Interestingly, this means you can reassign a variable with
# a different data type unlike in other programming languages.
myVariable = 10         # An Integer
print("myVariable contains value " + str(myVariable))
myVariable = "oops"     # A String
print("myVariable contains value " + myVariable)
myVariable = True       # A Boolean
print("myVariable contains value " + str(myVariable))

# If you are trying to figure out what the type of a variable is
# you can accomplish this by using the type() function.
# Note: You will need to surround the type with a str() to output it to console.
print("The type of " + str(aBoolean) + " is " + str(type(aBoolean)))
print("The type of " + aString + " is " + str(type(aString)))
print("The type of " + str(anInteger) + " is " + str(type(anInteger)))
print("The type of " + str(aFloat) + " is " + str(type(aFloat)))

# Notice how in 1_ConsoleOutput and 2_VariablesAndDataTypes
# how we use the function str(). This is called *Type Casting*
# and is done to convert one value to another.
# Other type casting function exist such as int() and float()
myInt = "10"
print("Variable myInt contains a " + str(type(myInt)) + " with a value of " + myInt)
myInt = int(myInt)
print("Variable myInt now contains a " + str(type(myInt)) + " with a value of " + str(myInt))
