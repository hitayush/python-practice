class employee:

    def __init__(self, salary,Name, bond): #constructor
        self.salary = salary
        self.Name = Name
        self.bond = bond

    def getsalary(self): #method
        return self.salary
    

    def get_info(self):
        return f"Employee Name: {self.Name}, Salary: {self.salary}, Bond Period: {self.bond} years"
e = employee(100000, "Ayush", 2)
e1 = employee(150000, "Rahul", 3) #creating object of class employee
print(e.getsalary())
print(e1.getsalary())
print(e1.get_info()) #calling method using object
print(e.get_info())
