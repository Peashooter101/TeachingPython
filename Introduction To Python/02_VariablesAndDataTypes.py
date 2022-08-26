"""
Variables and Data Types
----
Sometimes we might use the same values multiple times or need to store a value to be edited later.

This is accomplished through the use of Variables.
"""

# In Python, there are a few values that can be directly entered into code. These values are known as literals.

print(True)         # True is a Boolean Literal
print("String")     # "String" is a String Literal.
print(10)           # 10 is a Integer Literal.
print(10.5)         # 10.5 is a Float Literal.

# Variables are names that refer to a value held in memory.
# For example, a variable "myAge" may refer to a value 24 in memory.
# This can be done by using the format:
#   variableName = expression
# An expression is some value or code that produces a value.
# The `=` is the assignment operator, it assigns the value on its left into the variable on its right.

myAge = 24              # The value of 24 is assigned to myAge.
myWeight = 10 + 5.2     # The expression "10 + 5.2" results in 15.2, which is assigned to myWeight.

# Variables must be declared and have a value assigned before you use them.

print(myAge)            # myAge references to the value 24 in memory.
print(myWeight)         # myWeight references to the value 15.2 in memory.

# Variable names need to be spelled correctly, otherwise they cannot be referenced later in the code.
# Variable names are also case-sensitive. You cannot use any of Python's keywords as a variable name either.
# Variables must also not start with a digit.

# There are a few standard data types in Python. They can all be stored and represented in variables.
# As shown earlier, the values types can be represented with Literals.

aBoolean = True     # Used to store a True / False (Yes or No) Value
aString = "String"  # Used to store text.
anInteger = 10      # Used to store whole numbers.
aFloat = 10.5       # Used to store numbers with fractional pieces.

# Variables in Python are implicit, meaning you do not specify the specific data type,
# it is implied by the value you assign to it.
#
# For example in Java (explicit type declaration), you will say `int myInt = 10;`
# However in Python (implicit type declaration), you will say `myInt = 10`
#
# This also means you can reassign a variable with a different data type unlike in other programming languages.

myVariable = 10         # An Integer
print("myVariable contains value", myVariable)

myVariable = "oops"     # A String
print("myVariable contains value ", myVariable)

myVariable = True       # A Boolean
print("myVariable contains value", myVariable)

# You can use type() to get the data type of the value / variable.

print("The type of", aBoolean, "is", type(aBoolean))
print("The type of", aString, "is", type(aString))
print("The type of", anInteger, "is", type(anInteger))
print("The type of", aFloat, "is", type(aFloat))

# Notice how in 1_ConsoleOutput and 2_VariablesAndDataTypes
# how we use the function str(). This is called *Type Casting*
# and is done to convert one value to another.
# Other type casting function exist such as int() and float()

myInt = "10"            # A String
print("Variable myInt contains a", type(myInt), "with a value of", myInt)

myInt = int(myInt)      # An Integer
print("Variable myInt now contains a", type(myInt), "with a value of", myInt)

"""
Summary
-----
Variables are a necessary component of programming because they let us store values and use them again and again.
You can assign a variable using =.
    variableName = Value

Data Types describe the kind of value the variable holds and can be extracted by using type().
    String      - Holds Text
    Integer     - Holds Whole Numbers
    Floats      - Holds Numbers with Fractional Pieces
    Booleans    - Holds a True or False Value
    
And you can convert them between each other using their respective casting functions:
    str()       - Convert to String
    int()       - Convert to Integer
    float()     - Convert to Floating Point Value
    bool()      - Convert to Boolean
"""
