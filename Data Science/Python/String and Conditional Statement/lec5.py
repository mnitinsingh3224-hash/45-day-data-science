age = int(input("Enter your age"))
if(age>18 and age < 55):
    print("You are elgible to vote")
elif(age>55):
    print("You are overaged")
else:
    print("You are not elgible to vote")

#Match case Staments:
#It is not necessary to add break and continue statement in python.

fruit = input("Enter a fruit: ")

match fruit:
    case "apple":
        print("Red fruit")
    case "banana":
        print("Yellow fruit")
    case "mango":
        print("King of fruits")
    case _:
        print("Unknown fruit")