#class: class is a blue print for creating objects.
#object: object is an instance of a class.


class employee: #def __init__(self): #constructor
    company = "Google"
    def getsalary(self): #method
        return 100000


e=employee() #creating object of class employee
print(e.getsalary()) #calling method using object

e2=employee()
print(e2.getsalary())