"""
Outputting to the Console
---
By using the print() function, you can go ahead and print anything to the console.
Generally things sent to the console must have a *String* representation.

print(something), where "something" is known as an argument (arg) or parameter (param).
"""

# The following code outputs "Hello World!" to the console.
# Putting text between either single or double quotes creates a String Literal.
# This simply is just "literally this text".

print("Hello World!")

# Notice that the console will automatically start a new line after you use print().

print("This is on it's own separate line.")

# You can combine different string literals together using +
# More details about this will be discussed later.
# These will essentially connect the two strings exactly.

print("This is the first part, " + "and this is the second part")
print("Notice how these two parts" + "don't have a space in between")

# If you wanted to use quotes in your print output, you will need to escape them.
# This is done using the \ key.

print("This piece of \"code\" has quotes!")

# Literal numbers can be easily converted into strings on the fly for use in print().
# You can also do this with most types of data.

print(10)

# Although if you are printing something like a string and an int in the same line,
# sometimes you will need to convert the other values into a string using str().

print("This thing is a number -> " + str(10))

# You can also print this using multiple arguments like so...

print("This thing is a number ->", 10)

# In the above example, notice that Python automatically uses a space to separate the two arguments.

# You can also choose your own separator (the default separator is space).

print("This thing is a number", 10, sep=" -> ")

# This effectively does the same thing as the previous print command, but the separator is -> now.
# sep is known as a Keyword Parameter. Keyword parameters will be discussed later.

"""
Summary
-----
Console Outputs are fairly simple but are necessary for a way to show what code is doing.

Console Output can be done through print() and you provide some value into the parenthesis, typically a String.
    print("Hello World!")

A String Literal is some text between quotes.
    "This is a String Literal"
    
And you can turn other things into strings with str().
    str(10)
"""
