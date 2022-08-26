"""
Condition Statements
-----
Now to make use of all those operators.

Condition Statements are statements and blocks of code that can execute if a condition is True.
They rely on the usage of Comparison and Logical Operators to work, both of which output Boolean values.
"""

# Code blocks are designated by their indentation, so indentation in Python is INSANELY important.
# Do not screw up your indentation.
#
# A block of code is just code, but grouped up.
#
# The keyword "if" is used to start a condition block.

if True:
    print("This code will execute because \"if (True):\"")
if False:
    print("This code will not execute because \"if (False):\"")

# Your IDE will be highlighting the second print statement, saying it is wrong because the code is unreachable.
# It is unreachable because the condition is always false.
# An if statement will only execute the code block if the condition is True.

# You can chain these if statements together using elif ("else if") and else:
#   elif will execute if the above conditions are false but its is true
#   else will execute if the above conditions are all false

if False:
    print("This code will not execute because \"if (False):\"")
elif True:
    print("This code will execute because \"elif (True):\"")
else:
    print("This code will not execute because a condition above it is True")

if False:
    print("This code will not execute because \"if (False):\"")
elif False:
    print("This code will not execute because \"elif (False):\"")
else:
    print("This code will execute because all conditions above it are False")

# Note that:
# All condition statement chains will begin with an "if". There can only be one "if" in a chain.
# "elif" must always come after "if" in a chain. This can be the end of a chain, but cannot come after else in a chain.
# "else" must always be the last condition statement in a chain. There can only be one "else" in a chain.

# Let's put everything together. Here is a simple program that will ask for a number from the user.
# If it is larger than 50, say it's big.
# If it is not, but it is larger than 25, say it's small.
# If neither is the case, say it's tiny.

# Take user input and turn it into a number.
myNumberInput = int(input("Please give me a number: "))
# If it is bigger than 50,
if myNumberInput > 50:
    # say it's big.
    print("The number is big!")
# If it is not, but it is bigger than 25,
elif myNumberInput > 25:
    # say it's small.
    print("The number is small!")
# If neither is the case, say it's tiny.
else:
    # say it's tiny.
    print("The number is tiny!")

"""
Summary
-----
Conditional Statements are statements that check Boolean values and execute if their conditions are met.

All chains of conditional statements will start with if.
If the condition is true, the code block will execute.
    if (condition):

elif is used in case the above statements fail. Also known as "else if",
if the above conditions are false but this one is true, the code block will execute.
    elif (condition):

else is used as the last part in a chain of conditional statements.
If all the above conditions are false, the code block will execute.
There is no other condition check.
    else:
"""
