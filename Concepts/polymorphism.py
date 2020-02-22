# Polymorphism
## **Polymorphism:**
### same function name being uses for different types.
### using an operator or function in different ways for different data inputs.

# Inbuilt Polymorphic function:
print(len("polymorphism"))
# this prints the number of letters in the word polymorphism

# Defined Polymorphic function:
def add(a, b, c = 0):
    return a + b + c
# this adds a, b, and c together and initially, sets the value of these to 0.
print(add(3, 6))
print(add(3, 6, 9))
# this tells the program to put the number 3 into value a and number 6 into value b and add them
# this tells the program to put the number 3 into value a, number 6 into value b, number 9 into the value c and add them