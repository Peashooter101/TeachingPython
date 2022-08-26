"""
Logical Operators
-----
MORE OPERATORS! When will it end...

Logical Operators cover the ideas of "logic" and operate on boolean values.

What is "logic"? Well if something is "Not True" it's "False" right?

There are three main Logic Operators and one additional one we will discuss:
    not, and, or, ^ (Exclusive OR)
"""

# Logical Operators mainly work on Boolean values and are pretty much right what they say on the tin.
# The first operator we will discuss is NOT. NOT inverts the boolean value.

boolean1 = not True
print("\"not True\" is", boolean1)

# AND and OR both operate on two booleans and compare the values. They should do exactly what it says on the tin.
# Since there are 2 values to a Boolean, and we are comparing them, there are a total of four possible outcomes.

# AND should output True if both Booleans are True.

boolean2 = False and False
print("\"False and False\" is", boolean2)
boolean3 = False and True
print("\"False and True\" is", boolean3)
boolean4 = True and False
print("\"True and False\" is", boolean4)
boolean5 = True and True
print("\"True and True\" is", boolean5)

# OR should output True if either Booleans are True.

boolean6 = False or False
print("\"False or False\" is", boolean6)
boolean7 = False or True
print("\"False or True\" is", boolean7)
boolean8 = True or False
print("\"True or False\" is", boolean8)
boolean9 = True or True
print("\"True or True\" is", boolean9)

# Finally, there is Exclusive OR, shorthanded to XOR.
# XOR is unique in that exclusively one or the other is True, but not both.
# If A and B are both Booleans, XOR can be represented as:
#   (A or B) and not (A and B)
# So why is there no keyword for XOR? Well ^ is known as Bitwise XOR but that part is not important right now.

boolean10 = False ^ False
print("\"False ^ False\" is", boolean10)
boolean11 = False ^ True
print("\"False ^ True\" is", boolean11)
boolean12 = True ^ False
print("\"True ^ False\" is", boolean12)
boolean13 = True ^ True
print("\"True ^ True\" is", boolean13)

# Oh, and just for the record, you can chain these together and have their own order of operations:
#   not -> and -> or
# As always, parenthesis will group them together and take the highest precedence.

boolean14 = (False or True) and not(True and True)
# TODO for you: What is the value of boolean14? True or False?

# Alright, this is a fair bit of information on operators. Maybe now we can do something with it?

"""
Summary
-----
Logical Operators are operators that work on Booleans, they help with the logic handling of programs.
    not (Inverts the value)
    and (Both must be true to be true)
    or  (Either must be true to be true)
    ^   (Exclusive OR, Either must be true but not both, to be true)
"""
