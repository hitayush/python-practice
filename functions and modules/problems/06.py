list=[1, 2, 3, 4, 5]
def map():
    squared_list = [x**2 for x in list]
    return squared_list

result = map()
print(result)