class Animal:
    def sopund(self):
        print("Some generic animal sound")

class dog(Animal):  # Inherit the sopund method from Animal
    def sopund(self):
        print("Bark")

class cat(Animal): # Override the sopund method
    def sopund(self):
        print("Meow")

d=dog() # Create an instance of dog
d.sopund()
c=cat() # Create an instance of cat 
c.sopund()

