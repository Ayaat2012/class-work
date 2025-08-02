# empty dictionary 
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'flower', 2: 'light'}

# dictionary with mixed keys
my_dict = {'name': 'Ria', 1: [1, 3, 2, 4]}
my_dict = {'name': 'Haze', 'age': 18}

# output: Haze
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 19
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# removing particular element
my_dict.pop('age')
print(my_dict)

# access a particular element
print("Address :", my_dict.get('address'))

# removing all the elements
my_dict.clear()
print(my_dict)