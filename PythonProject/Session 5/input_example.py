name = input("Enter your name: ")
print("hello", name)
age = input("Enter your age: ")
try:
    age = int(age)
    print("you were born in", 2025-age)
except ValueError:
    print("I am sorry", name, "but that is not a real number")
except ZeroDivisionError:
    print("you can't divide by zero")
else: #esle is only when no exception happens
    print("thank you for playing fair")
finally:
    print("End of game") #this one happens no matter what
