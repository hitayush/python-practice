class employee:

    def __init__(self, salary,Name, bond): #constructor
        self.salary = salary #creating an instance attribute of name salary
        self.Name = Name
        self.bond = bond

    def getsalary(self): #self is imporatnt to access the attributes and methods of the class
       
        return self.salary
    

    def get_info(self):
        return f"Employee Name: {self.Name}, Salary: {self.salary}, Bond Period: {self.bond} years"
e = employee(100000, "Ayush", 2)
e1 = employee(150000, "Rahul", 3) #creating object 
e2= employee(200000, "Divea", 10)
print(e.getsalary())
print(e1.getsalary())
print(e1.get_info()) #calling method using object
print(e.get_info())
print(e2.get_info()) #calling method using object


class Dog:
    def __init__(self, name, breed):  # The constructor
        self.name = name      # Setting the name attribute
        self.breed = breed    # Setting the breed attribute

# When we do this:
my_dog = Dog("Fido", "Poodle")  # The __init__ method is automatically called

# It's like we're saying:
# 1. Create a new Dog object.
# 2. Run the __init__ method on this new object:
#    - Set my_dog.name to "Fido"
#    - Set my_dog.breed to "Poodle"
class Dog:
    def __init__(self, name="Unknown", breed="Mixed"):
        self.name = name
        self.breed = breed

dog1 = Dog()          # name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rex")     # name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be "Labrador"