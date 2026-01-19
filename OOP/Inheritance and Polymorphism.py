class Animal: #parent class
    location = "Earth"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


class dog(Animal):
    def speak(self):
        super().speak()  # calling the speak method of the parent class
        print("woof woof")


#a = Animal("Dog")
# a.speak()

d = dog("TARS")
d.speak()  # will print "woof woof" because the speak method in dog class overrides the speak method in Animal class
print(d.location)  # will print "Earth" because dog class inherits location attribute from Animal class


class cat(Animal):
    location = "Mars"  # overriding the location attribute of the parent class
    def speak(self):
        print("meow meow")
c = cat("Kitty")
c.speak()  # will print "meow meow"
print(c.location)  # will print "Earth" because cat class inherits location attribute from Animal class

#super() function is used to call the constructor of the parent class

class lion(Animal):
    def __init__(self, name, pride_size):
        super().__init__(name)  # calling the constructor of the parent class
        self.pride_size = pride_size

l = lion("Simba", 10)
print(l.name)  # will print "Simba"
print(l.pride_size)  # will print 10