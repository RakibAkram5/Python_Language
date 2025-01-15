value = input("Input some comma-separated numbers: ")  
numbers_list = value.split(",")  
numbers_tuple = tuple(numbers_list) 

print("List: ", numbers_list)
print("Tuple: ", numbers_tuple)
