class Animal:
    def __init__(self,name):
        self.name = name
        def speak(self):
            print("Animal speaks")


class Dog(Animal): # Inheriting from Animal class
    def speak(self): # Overriding the speak method
        print("Woof!")

a=Animal("Dog")
a.speak()