class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self,v):
        return vector(self.x + v.x, self.y + v.y)
    
    def print_vector(self):
        print(f"Vector({self.x}, {self.y})")

    def __add__(self, v):
        return vector(self.x + v.x, self.y + v.y)


p1 = vector(1, 2)
p2 = vector(3, 4)
# Adding two vector objects using operator overloading
p= p1.sum(p2) # will return a new vector object with x=4 and y=6
p.print_vector()  # will print "Vector(4, 6)"

p= p1 + p2  #we overlaoded the + operator to add two vector objects
p.print_vector()  # will print "Vector(4, 6)"