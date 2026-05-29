#String -> a string is simply a sequence of character enclosed in quotes.
name = "nitin"
friend = "ram"

apple = ''' He said, hi nitin singh 
i am good "i want to eat an apple'''

print("Hello" , name)
print(apple)

for character in name:
    print(character)

#Operation on String

names = "Nitin , Singh"
print(names[0:5])
print(len(names))

print(names[0:-3]) # ->  so 5- 3 gives 2 -> [0:2]
print(names[-3:-1]) # -> so 5 - 3 = 2 and 5 - 1 = 4 -> so it gives [2:4]

# Strings are immutable

a = "Nitin"
print(len(a))
print(a.upper())  # gives different string not real one
print(a.lower())
b = "Nitin!!!!!!"
print(a.rstrip("!"))
print(a.replace("Nitin" , "Ram"))
print(b.split(" ")) # basically gives space between them
blogheading = "introduction to jS"
print(blogheading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50))) # it basically gives the steps
print(a.count("Nitin"))
print(str1.endswith("to", 4 , 10)) # Is to ending with 4 to 10 length of string. 
print(str1.find("the")) 
#print(str1.index("ishh")) return value error
print(str1.isalum()) # it true only if it consist with a-z , A-Z , 0 - 9
print(str1.isalpha()) # it true only if it consist with a-z , A-Z 
print(str1.islower())
print(str1.isspace())
print(str1.isprintable())
print(str1.istitle())
print(str1.swapcase())
print(str1.title())
