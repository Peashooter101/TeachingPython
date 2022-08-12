"""
Lists
-----
So it's cool that you can now make actual programs and what not.

But what if we need an arbitrary amount of things stored in
the same place? Making a thousand variables and holding everything
in there seems insanely inefficient. That is like... Having a piece
of notepad paper for each item you want to buy at the store...

Why don't you just write them down on the same paper as a *List*?
"""

# Lists are a form of data structure (container used organize / represent data).
# Lists in Python can contain any number of things and of all different data types!
#   In other languages like Java, you can only store things of the same type in a list.
#
# Lists can literally be made as shown below.
# And a whole list can be printed directly.

myList = [10, "April", True]
print("myList: " + str(myList))

# Lists can be iterated through using for loops. Same idea as using range().

for i in myList:
    print("myList Item: " + str(i))

# If you need an empty list, you can create one literally or use the *List Constructor*

emptyList = []
print("Empty List Literal: " + str(emptyList))
emptyList = list()
print("Empty List Constructor: " + str(emptyList))

# Items in a List can be indexed. Indexes start at 0 and go up to the size - 1.
# You can use the format List[index] to get the item at that index.
# Each specific item is known as an *element*.

print("myList Item 0: " + str(myList[0]))
print("myList Item 1: " + str(myList[1]))
print("myList Item 2: " + str(myList[2]))

# And you can directly edit an indexed value.

myList[0] = myList[0] * 2
print("myList Item 0 Edited: " + str(myList[0]))

# Lists can have things added or removed from them.
# List.append(item) will add item to the list.
# List.remove(item) will remove that item from the list.

myList.append("Something New")
myList.remove("April")

print("myList after Append and Remove: " + str(myList))

# Note that you can also append variables onto the lists.
# Although, what is stored is the value stored in the variable,
# not the variable itself.

myString = "Wowza"
myList.append(myString)

print("myList after Appending variable: " + str(myList))

# You can also have duplicates elements within lists.

myString = "Wowza"
myList.append(myString)

print("myList after Appending variable again: " + str(myList))

# Finally, a little advanced but there is something called List Comprehension.
# In this example, we can use a for loop to automatically generate a list.
# We put the initial i as the value that gets assigned.

listComp = [i for i in range(10)]
print("List Comprehension: " + str(listComp))

# To further demonstrate the use of the first i, this List Comprehension
# will multiply the value of i by 2.

listComp = [i*2 for i in range(10)]
print("List Comprehension x2: " + str(listComp))
