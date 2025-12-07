student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])  # Access value by key
student["grade"]= "A+"  # Modify value
print(student)
student["city"]= "New York"  # Add new key-value pair
print(student)
del student["age"]  # Remove key-value pair
print(student)