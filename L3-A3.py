class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Parrot class
blu = Parrot("blu", 10)
woo = Parrot("woo", 15)

# Access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# Access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("And {} is {} years old".format( woo.name, woo.age))