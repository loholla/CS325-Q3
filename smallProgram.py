import random
print ("This is our small program for the quiz")

print ("Not a 'Hello, World!' program")
numberInput = int(input("Enter a number between 1 and 10\n"))
randNum = random.randint(1, 10)
newNumber = randNum + numberInput
text = f"This is your new number, which is obtained by taking your provided number, '{numberInput}', and using a randomly generated number, '{randNum}', and adding them together, is equal to '{newNumber}'"
print(text)