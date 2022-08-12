"""
Loops
-----
So let's say you wanted to do something multiple
times. Well right now, your current solution will be
to just go:
    print(A)
    print(B)
    print(A)
    print(B)
    ... and so on ...

So let's introduce looping to let you do the same things
over and over again in a compact and not hard-coded way!
"""

# Loops are similar to condition statements, they execute
# code if told to, fairly straight forward.
#
# First, the while loop. As long as the condition is True,
# code within the while loop will execute.
#
# In this case, the code should output the value of myNum
# from values 10 to 1.

myNum = 10                                      # Counting Variable
while (myNum != 0):                             # While the number isn't 0...
    print("myNum is currently " + str(myNum))   # Print a message to console with the number's value.
    myNum = myNum - 1                           # Decrement the value by 1.
print("The while loop above is done!")          # This line does not execute until the while loop exits.

# While loops can also continue early or exit early
# by using a few other keywords.
#
# "break" will exit the loop immediately.
# "continue" will stop this *iteration* of the loop, but continue the while loop.
#   An *iteration* in this context is just a "run through the loop".
#
# In this case, the output should be the values 10 to 5, then 2 to 0.
# Values 4 - 3 are skipped because of the first if statement.

myNum2 = 10                                         # Counting Variable
while (True):                                       # Will execute at least the first time.
    if (myNum2 == 5):                               # If the number is 5, example of continue
        print("myNum2 is 5! Setting value to 2!")
        myNum2 = 2
        continue
    print("myNum2 != 5. myNum2 is " + str(myNum2))
    myNum2 = myNum2 - 1
    if (myNum2 == 0):                               # If the number is 0, example of break
        print("myNum2 is 0! Breaking!")
        break

# While loops are very useful in many kinds of code execution
# and allow for you to have code execute many times without
# having to manually hard code and type it out each time.
