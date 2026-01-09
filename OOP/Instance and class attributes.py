class employee:
    company = "google" #class attribute 

    def __init__(self,salary,name,bond,company): #constructor

        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company # Instance attribute overriding class attribute
    def getsalary(self):
        return self.salary
    
    def get_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}, Bond Period: {self.bond} years"

e1 = employee(100000,"Ayush",2, company="Amazon") #creating object

print(e1.company) # will print "Amazon" because instance attribute overrides class attribute and this will always print the instance attribute if it exisits 
