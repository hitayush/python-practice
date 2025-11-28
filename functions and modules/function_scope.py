def su (a,b):
    c=a+b
    global z #modifying the global variable
    z=1 #local variable then after this will refer to global variable
    return c

def greet():
    z= 32
    print("Hello, World!")

z=8 #this is a global variable
print(z)
print(su(2,3))
print(z)
greet()
print(z)
greet() #calling the function