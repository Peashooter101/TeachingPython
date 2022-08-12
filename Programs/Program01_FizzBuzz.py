"""
FizzBuzz
-----
FizzBuzz is a number counting game played by children.

The rules are as follows:
- If the number is divisible by 3, say "Fizz"
- If the number is divisible by 5, say "Buzz"
- If the number is divisible by both, say "FizzBuzz"
- If the number is divisible by neither, just say the number.
"""

maxNumber = int(input("Count up to what number? "))

for i in range(1, maxNumber+1):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)

# This isn't a great way of implementing this for a few reasons:
# - This is not easily expandable.
#   Adding even 1 more rule like "A number divisible by 7, say *Bizz*" would be a lot.
# - There are a lot of redundant checks.
#   You are checking the same conditions twice.
#
# There is a much better way that fixes the above problems, can you think of it?
