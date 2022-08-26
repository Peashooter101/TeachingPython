"""
Inputting to the Console
---
Taking user input in some form is one of the most important parts of a program.
If there is no user input, then how does a program expect to interact with the person using it?
"""

# Taking an input is as simple as using the input() function. All inputs by default will become a String.
# We will use print() to tell the user we are waiting for them.

print("Please type something below: ")
myInput = input()
print("You typed in:", myInput)

# In the above example, we used print() to prompt the user that we are waiting for input.
# However, we can accomplish this by providing a string to the input() function.

myInput = input("Please type something here: ")
print("You typed in:", myInput)

# Notice that by providing the prompt in input(), the prompt is in-line (on the same line) as the input.
# However, only the user input is stored in the variable.

# If you need another type from the input, just use type casting, as discussed in 2_VariablesAndDataTypes

myInputNumber = int(input("Please give me a number: "))
print("myInputNumber has type", type(myInputNumber), "and a value of", myInputNumber)

# Notice, if you provide something that cannot be cast into an integer, this will throw an error.
# Error Handling will be discussed in a future section.

"""
Summary
-----
Taking input from the console is simply by using input().
The value coming back from input() is in the form of a String.
    variableName = input()
    
You can provide a message to prompt the user for input by providing a String in the parenthesis.
    variableName = input("Prompt: ")
"""
