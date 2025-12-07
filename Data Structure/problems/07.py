my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output will be {1, 2, 3, 4} since sets do not allow duplicates

my_set.add(5) # Add element
print(my_set)
my_set.remove(2) # Remove element
print(my_set)

print(4 in my_set)  # Check membership