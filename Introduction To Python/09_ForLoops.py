"""
For Loops
-----
A little backwards to teach While and then For loops, but
needed the foundational ideas for loops, since Python does
loops a little bit differently.

Most for loops you will use in Python are like "for-each"
loops. Each value in a given group of elements will be executed.
"""

# range() is a method that adds number counting similar to
# what we had for the while loop. They will produce integers
# from the minimum up to less than the maximum, incremented
# by some given value.
#   range(max)              will start from 0,      increment by +1,    and end before max.
#   range(min, max)         will start from min,    increment by +1,    and end before max.
#   range(min, max, inc)    will start from min,    increment by inc,   and end before max.
# For example:
#   range(1, 10, 2) will iterate through the values [1, 3, 5, 7, 9]
#
# "in" is a keyword that will go through the iterations provided by an iterable object.
#   These things include range and, something for the future, lists.
#
# "for" will set up the entire loop and put the value into an iterator variable that you
# designate.
#
# So... With all that information, consider the following code...

for i in range(10):
    print("For Loop's i is " + str(i))

# As noted, it loops ten times, as it iterates through the values:
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# and through each iteration, stores it in the variable "i".
#
# Your brain melted yet? Good...
#
# You can also edit the value of i, but i will get reassigned each time the loop restarts.

for i in range(5):
    print("The value of i is " + str(i))
    i = 100
    print("Reassigned value of i to " + str(i))

# Now consider the break and continue that we used in while loops.
# Those can also be applied to for loops.

for i in range(1, 11):                              # Loop for the values 1 through 10...
    if (i % 2 == 0):                                # For even numbers...
        print("Even Number! Continue!")
        continue
    if (i == 9):                                    # Exit the loop when i == 9
        print("Nine! Break!")
        break
    print("The current value of i is " + str(i))

# Normally, without the condition statements, the output would
# count the values from 1 through 10. With the conditionals,
# all even numbers will continue the loop without outputting the value
# and 10 does not even get shown because the loop is broken when i is 9.
#
# Okay, your brain broken yet? AWESOME!

"""
Summary
-----
For loops are blocks of code that keep
executing so long as there is still more
things to execute off of.
    for variable in iterable:
    
You can use the variable's name to access
the current element for that iteration of
the loop.
    for varName in iterable:
        print(varName)
    
Something iterable includes range() which
can be used to produce numbers for the loop.
    for i in range(1, 10, 2):
        Produces [1, 3, 5, 7, 9] for the loop.
"""
