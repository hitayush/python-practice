my_tuple=(10,20,30,40,50)

my_list=list(my_tuple) #convert tuple to list
my_list.append(50) #add element to list
print(my_list) 

my_tuple+tuple(my_list) #concatenate tuple with converted list
print(my_tuple)