"""
Outputting to the Console
---
By using the print() function, you can go ahead and
print anything to the console. Generally things sent
to the console must have a *String* representation.

print(something), where "something" is known as an
argument / arg or parameter / param.
"""

# Outputs "Hello World!" to the console.
# Putting text between either single or double quotes
# creates something called a *String Literal*.
# This simply is just "literally this text".
print("Hello World!")
# Notice that the console will automatically start a
# new line after the print call.
print("This is on it's own separate line.")

# You can combine different strings together using +
# More details about this will be discussed later.
# These will essentially connect the two strings exactly.
print("This is the first part, " + "and this is the second part")
print("Notice how these two parts" + "don't have a space in between")

# If you wanted to use quotes in your print output,
# you will need to *escape* them. This is done using
# the \ key.
print("This piece of \"code\" has quotes!")

# Literal numbers can be easily converted into
# strings on the fly for use in print().
print(10)

# Although if you are printing more than just a
# single argument, sometimes you will need to convert
# the other values into a string using str().
print("This thing is a number -> " + str(10))
