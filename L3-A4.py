class Parrot:

    # Instance attributes
    # Constructor method - special method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def sing(self, song):
        return ("{} sings {}".format(self.name, song))
    
    def dance(self):
        return ("{} is now dancing".format(self.name))
    
# Instantiate the object
blu = Parrot("blu", 10)

# Call our instance methods
print(blu.sing(" 'Happy' "))
print(blu.dance())