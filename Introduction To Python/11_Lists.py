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
# Each specific item is known as an element.

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

# And we can also check if something is in a list using the keyword "in".

inList1 = "BLEP" in myList
print("\"BLEP\" in myList = " + str(inList1))
inList2 = "Wowza" in myList
print("\"Wowza\" in myList = " + str(inList2))

# And we can also insert an element at any position in the list.
# Insertion works by using an index as a reference.
# Everything from that index and onward is pushed forward and
# the object is fit into the spot.
#
# Remember, all indexes start at 0.

insertList = [1, 2, 4, 5]
print("insertList before insert: " + str(insertList))
insertList.insert(2, 3)
print("insertList after insert:  " + str(insertList))

# Finally, a little advanced but there is something called List Comprehension.
# In this example, we can use a for loop to automatically generate a list.
# We put the initial i as the value that gets assigned.

listComp = [i for i in range(10)]
print("List Comprehension: " + str(listComp))

# To further demonstrate the use of the first i, this List Comprehension
# will multiply the value of i by 2.

listComp = [i*2 for i in range(10)]
print("List Comprehension x2: " + str(listComp))

# Lists just provide a very useful way to store arbitrary amounts of
# data without having to make a million variables. Let us see it in action
# alongside an example function!

shoppingStock = ["Apple", "Apple", "Dog", "What"]
shoppingList = ["Apple", "Apple", "Apple"]

print("Before Shopping:")
print("  Shopping Stock: " + str(shoppingStock))
print("  Shopping List:  " + str(shoppingList))


def shop_items(shoppingListArg):
    returnCart = []
    for item in shoppingListArg:
        if item in shoppingStock:
            shoppingStock.remove(item)
            shoppingList.remove(item)
            returnCart.append(item)
    return returnCart


shoppingCart = shop_items(shoppingList)
print("After Shopping:")
print("  Shopping Stock: " + str(shoppingStock))
print("  Shopping List:  " + str(shoppingList))
print("  Shopping Cart:  " + str(shoppingCart))

"""
Summary
-----
Lists are data structures that hold elements.
The elements can be of any type. Empty lists
can be made with list() or [].
    fish = [1, 2, "Red", "Blue"]

Lists are ordered and can be elements can be
edited and changed.
    list[index]         Accesses element of list at position index.
    list.append(x)      Adds element x to list.
    list.remove(x)      Removes element x from list.
    list.insert(pos, x) Inserts element x at index pos.
    
Lists can also:
- Contain duplicate items.
- Be iterated through like in a for loop.

List Comprehension is when a List can generate values using
some internal for loop or other iterable means.
    [i for i in range(5,10)]
"""
