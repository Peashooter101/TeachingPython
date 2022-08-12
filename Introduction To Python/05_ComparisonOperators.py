"""
Comparison Operators
-----
Alright so our code can now do math that we
could do in our heads. Big deal right? Still
we are fairly limited in what we can do.

So let's talk about a few other kinds of operators.
This time, *Comparison Operators*.

Here are 6 of them:
    <, <=, >, >=, !=, ==
"""

# Comparison operators compare two values together.
# Hence, the name. This means they will answer a
# Yes or No question. For example, is 5 bigger than 4?
compare1 = 5 > 4
print("\"5 > 4\" is " + str(compare1))

# So as you can guess, it outputs a value of True or False,
# also known as a Boolean. Each of these pretty much matches
# what you learned in math class.
# >  (Greater Than)     >= (Greater Than or Equal To)
# <  (Less Than)        <= (Less Than or Equal To)
# == (Equals)           != (Does not Equal)
compare2 = 5 < 5
print("\"5 < 5\" is " + str(compare2))
compare3 = 5 <= 5
print("\"5 <= 5\" is " + str(compare3))
compare4 = 4 == 3
print("\"4 == 3\" is " + str(compare4))
compare5 = 4 != 3
print("\"4 != 3\" is " + str(compare5))

# This may not seem very useful yet, but it will be soon.
# Although before we can see why it's useful, we will
# Need to cover Logical Operators.
