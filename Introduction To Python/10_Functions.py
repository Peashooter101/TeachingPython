"""
Functions
-----
What if you want to organize and develop code and make it more readable?

What if you want to group similar tasks or reusable blocks of code into
something that makes sense?
"""

# Functions are definitions of blocks of code that do things when called.
# You declare a function with the keyword "def" and give it a name.
# Much like any function call you've done before, parenthesis are involved.
# We will talk about what can go in there later, for now here is a simple one.


def simple_hello():
    print("Hello World!")


# Now that you have that little code block, you can now call it from wherever.
# Sort of... It has to be called AFTER it is defined.
# If you call it before it's defined, it will throw an error.

simple_hello()

# Well that's cool! But what if I wanted to do more?
# The arguments or parameters go inside the parentheses.


def say_hi(name):
    print("Hello " + str(name) + "!")


say_hi("John")

# With multiple parameters, you can enter the parameters by listing
# them in the same order as they are in the method definition.


def two_args(arg1, arg2):
    print(arg1 + " " + arg2)


two_args("one", "two")

# You can also put them out of order, but call to the specific parameter
# using the parameter's variable name.

two_args(arg2="two", arg1="one")

# You can assign default values for when an argument isn't provided.


def default_values(arg1="no", arg2="value"):
    print(arg1 + " " + arg2)


default_values()
default_values("one")

# Functions can also *return* values based on your inputs!
# These return values are sent back to the caller for use!


def sum_of_numbers(num1=1, num2=5, num3=10):
    return num1 + num2 + num3


print("sum_of_numbers with defaults: " + str(sum_of_numbers()))
print("sum_of_numbers setting num1 with 10: " + str(sum_of_numbers(num1=10)))


# You can document things about a method by using
# block comments right after the function definition.
# You can look up more information about this but check
# out this example.


def documenting_function(arg1):
    """
    An example of documenting a method.
    :param arg1: Describe the parameter or expected value.
    :return: Describe the value of the return.
    """
    print("Documenting: " + str(arg1))
    return 0
