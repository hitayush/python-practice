#define a function to calculate average of three numbers
def average(a,b,c):
    d=(a+b+c)/3
    return d
output1=average (2,4,6)
outoput2=average (10,20,30)
print (output1) 
print (outoput2)

#function arguments and return values

def add(a, b):
    return a + b

print(add(5, 3))  

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) 

def add(x, y):
    s = x + y
    return s
    
result = add(10, 15)
print("The sum is:", result)



def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=19, name="Hitayush")