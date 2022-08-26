"""
Functions
-----
What if you want to organize and develop code and make it more readable?

What if you want to group similar tasks or reusable blocks of code into something that makes sense?
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
# You can provide arguments in order to provide inputs to specific kinds of functions!
# What each argument means depends on the parameters set by the function definition.
# The arguments or parameters go inside the parentheses.


def say_hi(name):
    print("Hello", name, "!")


say_hi("John")

# With multiple parameters, you can enter the parameters by
# listing them in the same order as they are in the method definition.


def two_args(arg1, arg2):
    print(arg1 + " " + arg2)


two_args("one", "two")

# You can also put them out of order, but call to the specific parameter using the parameter's variable name.

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


print("sum_of_numbers with defaults:", sum_of_numbers())
print("sum_of_numbers setting num1 with 10:", sum_of_numbers(num1=10))


# You can document things about a method by using block comments right after the function definition.
# You can look up more information about this but check out this example.


def documenting_function(arg1):
    """
    An example of documenting a method.
    :param arg1: Describe the parameter or expected value.
    :return: Describe the value of the return.
    """
    print("Documenting: ", arg1)
    return 0


# The biggest reason you will want to use functions is its ability
# to organize your code into much more useful smaller modules.
# This will make the main execution of your code look cleaner and easier to read.

"""
Summary
-----
Functions are blocks of code that can be called at a later time through their name.
They are defined using the word def.
    def function_name():
    
They are called using their function name.
    function_name()
    
You can define functions to have parameters and they can also have default arguments.
These arguments can be used in the function itself.
    def func_args(a, b=10):
        print(a + b)

You can return a value after the function is called to use in other parts of code later.
    def func_sum(a=10, b=10):
        return a+b
    variable = func_sum()
"""
