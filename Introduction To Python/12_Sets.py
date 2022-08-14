"""
Sets
-----
Sets are another way to store information and are very similar to
Lists, although there are some very big differences between the two.
"""

# Alright so first, empty set!
# You can construct an empty set using the set
# constructor set() or by using the literal set
# form {}.

emptySet = set()
print("Empty Set Constructor: " + str(emptySet))
emptySet = {}
print("Empty Set Literal: " + str(emptySet))

# Adding and removing is the same as a list, just
# with some different names.

mySet = set()
print("mySet: " + str(mySet))
mySet.add(2)
print("mySet: " + str(mySet))
mySet.remove(2)
print("mySet: " + str(mySet))

# Sets cannot have duplicate values, duplicates just
# get ignored when added!
#
# In this example, a list will be provided and converted
# into a set using set(). The argument for set() is just
# something that can be looped through (like a list).

givenList = list([2, 2**1, 1+1, 10-8])
outputSet = set(givenList)

print("List: " + str(givenList))    # Resulting List: [2, 2, 2, 2]
print("Set:  " + str(outputSet))    # Resulting Set:  {2}

# In a Set, elements are unordered.
# So you cannot access them with an index.
# But you can still iterate through them.
#
# Notice:   Every time you run the code, the unorderedSet
#           changes the order of its values! Order is not
#           guaranteed!

orderedList = ["Apple", "Banana", "Carrot", "Durian"]
unorderedSet = {"Apple", "Banana", "Carrot", "Durian"}

print("Ordered List:  " + str(orderedList))
print("Unordered Set: " + str(unorderedSet))

# You also cannot modify a specific element of a set.
# The elements are immutable, meaning they cannot be
# changed or modified. To "change a value in a set",
# you need to remove the original value, then add the
# new value. This cannot be done in a loop.

modifyingSet = {1, 2, 3, 4}
print("Original Set: " + str(modifyingSet))
modifyingSet.remove(1)      # Remove the original 1
modifyingSet.add(1*4)       # Add a 4, but the set already contains a 4 so its ignored.
print("Modified Set: " + str(modifyingSet))

"""
There are some major key differences between a list and set.

Duplicate Values:
    A list can contain duplicate values, but a Set cannot.
    Anything that you append, if it exists in the Set already,
    nothing really happens.

Ordering:
    A list is ordered and can be indexed (for example, myList[1]) but
    a Set is unordered and cannot be indexed. You can iterate through
    a Set but there is no guaranteed order for them.

Modification:
    Elements in a List can be modified, for example myList[1] = 10 but
    a set cannot be modified. Once it is in the set, it is in,
    and you have to explicitly remove it.
    
Looping:
    The size of a List can change while it is being looped through. If
    the size of a Set changes, an error is thrown. Both a List and Set
    can be loop through though.
"""
