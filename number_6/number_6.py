# Generate a list and tuple with comma-separated numbers

values = input("Input some comma separated numbers: ")
a_list = values.split(",")
a_tuple = tuple(a_list)
print(f"List: {a_list}")
print(f"Tuple: {a_tuple}")