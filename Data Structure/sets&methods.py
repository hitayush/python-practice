#creating a set and using methods
s={"apple","banana","cherry"}
s.add("orange")
print(s,type(s))
print(len(s))
s.remove("banana")
print(s)
s={34,23,1,3,22}

print(s)

s.add(32)
s.add(11)

print(s)
s.remove(1)
print(s)

s={"apple","banana","cherry"}
s.add("orange")
print(s,type(s))
print(len(s))
s.remove("banana")
print(s)

my_set = {1, 2, 3, 4}

my_set.add(5)        # {1, 2, 3, 4, 5}
my_set.remove(2)     # {1, 3, 4, 5}
my_set.discard(10)   # No error if element not found
my_set.pop()         # Removes random element