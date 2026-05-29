# List -> list are ordered collection of data items and they can be store multiple items in a single variable.

marks = [33,53,63,"Nitin",True]
print(marks)
print(marks[0])

#negative indexing
print(marks[-3])
print(marks[len(marks) - 3]) # make it positive

#Checking item in list
if 6 in marks:
    print("Yes")
else:
    print("No")

print(marks[1:]) #slicing is possible
print(marks[1:4:2]) # It is basically jump by value 2 in the string.

# list comprehension 
# This are used for creating new lists from other iterables like lists , tuples , sets , dictonaries even in arrays and strings
lst = [i*i for i in range(10)]
print(lst )
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)