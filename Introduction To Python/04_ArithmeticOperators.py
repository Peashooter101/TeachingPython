"""
Arithmetic Operators
-----
While getting input and outputting it the console is cool and all, it's not very useful on its own.
In fact, it's almost completely useless. So let's make them useful using Operators.

Operators make things happen.

There are seven math operators:
    + - / * % // **
"""

# All the operators shown above can be used in a math context:
#   + (Add), - (Subtract), / (Divide), * (Multiply), % (Modulo), // (Integer Division), ** (Exponent)
#
# All operators will follow some form of order of operations from left-to-right. The other of operations is
#   Exponentiation (**), then Multiplication / Division / Remainder (* / // %), then Addition / Subtraction (+ -)

someMath = 10 + 5 * 2
print("\"10 + 5 * 2\" is", someMath)

# You can use these operators with variables as well.

myNum1 = 10
myNum2 = 20
moreMath = myNum1 + myNum2
print("\"myNum1 + myNum2\" is", moreMath)

# You can perform an operation using a variable then reassign it to itself.

myNum3 = 10
print("\"myNum3\" is", myNum3)
myNum3 = myNum3 ** 2
print("\"myNum3 = myNum3 ** 2\" is", myNum3)

# Modulo is "remainder of", so it performs division on the two numbers and tells you how much is "left over".
# So for example,
#   5 / 2 = 2 remainder 1 (2*2 + 1 = 5)

myNum4 = 5 % 2
print("\"5 % 2\" is", myNum4)

# Interestingly, you can check if a number is divisible (perfectly divides) a number using modulo.
# If the modulo is 0, you know it perfectly divides that number.

myNum5 = 4 % 2
print("\"4 % 2\" is", myNum5)

# Integer Division is similar to division, except the fractional piece is thrown away.
# This is generally how integer divided by integer works in other languages like Java.
# Integer Division is also known as Floor Division.

myNum6 = 5 / 2
print("\"5 / 2\" is", myNum6)
myNum7 = 5 // 2
print("\"5 // 2\" is", myNum7)

# Most operands follow the order of operations while going left to right, however, exponents are an exception.
# If two ** operators share an operand, they execute right-to-left.

myNum8 = 2**3**4        # Evaluates to 2**(3**4)
print("\"2**3**4\" is", myNum8)
myNum9 = (2**3)**4
print("\"(2**3)**4\" is", myNum9)

# TODO: Perhaps put this in a separate file?
# These operators can also do other stuff too depending on the data type.
# For example, String + String is called String Concatenation. A fancy way of saying "connect them".

myStr1 = "Wow"
myStr2 = "So"
myStr3 = myStr1 + myStr2
print("\"myStr1 + myStr2\" is " + myStr3)

# In math, 1 + 2 = 2 + 1 but with Strings, the order does matter.

myStr4 = myStr2 + myStr1
print("\"myStr2 + myStr1\" is " + myStr4)

# What if you wanted to laugh... A lot... Like a psychopath?

myStr5 = "HA"
myStr6 = myStr5 * 100
print("\"myStr5 * 100\" is " + myStr6)

# There are a ton of other things these operators can do.
# These specific kinds of operators are generally called Arithmetic Operators,
# but clearly they can do more than just math.

"""
Summary
-----
There are a few basic operators, the five covered are:
    +  (Add)
    -  (Subtract)
    *  (Multiply)
    /  (Divide)
    %  (Modulo)
    ** (Exponent)
    // (Integer Division)
    
And these operators can do math as well as stuff for Strings:
    + will perform String Concatenation, combining them.
    * will multiply the String's value that many times.
"""
