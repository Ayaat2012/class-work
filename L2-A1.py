# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 6.13)
print(my_tuple)

# Nested tuple
my_tuple = ("mouse", [12, 6, 13], (2, 4, 6))
print(my_tuple)

# Nested index
n_tuple = ("mouse", [1, 2, 3], (4, 5, 6))

print(n_tuple[0][3])
print(n_tuple[1][1])

# Accessing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[4])
print(my_tuple[2])
print(my_tuple[3])

# Slicing
print("Sliced :", my_tuple[1:4])

# Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)