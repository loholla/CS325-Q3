import random
print ("This is our small program for the quiz")

print ("Not a 'Hello, World!' program")
numberInput = int(input("Enter a number between 1 and 10\n"))
randNum = random.randint(1, 10)
newNumber = randNum + numberInput

string = f"Your number got transformed into '{newNumber}' by adding '{randNum}' and '{numberInput}'."
print(string)