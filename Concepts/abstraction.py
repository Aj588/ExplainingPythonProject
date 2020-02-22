# Abstraction
## *Abstraction:**
### simplifying complex reality by making certain classes that are relative to the problem.

# abstract base class
from abc import ABC


class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can use my legs to walk and run")


class Snake(Animal):
    def move(self):
        print("I can use my body to squirm around")


class Cat(Animal):
    def move(self):
        print("I can meow")


R = Human()
R.move()

K = Snake()
K.move()

R = Cat()
R.move()

# Abstract classes allow for multiple functionality. If you look above, the class animal can have multiple different
# attributes to it. 