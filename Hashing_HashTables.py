'''
How much data
How many cells
Hash function

If we have 5 pieces of data we and 10 cells and 7 cells we would go with 7 cells - better for memory
For every 7 pieces of data we should have 10 cells

A Hash Table - is a data structure which maps keys to values using Hash functions, quickly look up values for a given key (super quick)

A Hash function - is a special function that takes an input - the key and returns a fixed sized string or integer - the output/values

Collision is when two keys have the same index

Load factor is a measure of how full the table is

'''

#Example how we would usually do it then compare to how we do it using a hash
def status_code(number):
    if number == 200:
        return "Ok"

    elif number == 301:
        return 'Moved'

    elif number == 401:
        pass


#This method would be so slow as the code has to go through each one, so we want to write it more efficiently

#Hash method:

# print(hash(200.10))
# print(hash(8225.50))
# print(hash("Hello"))



class Students:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __eq__(self, other): #This compares values
        return self.age == other.age and self.name == other.name


    def __hash__(self):
        print("The Hash is: ")
        return hash((self.age, self.name))


person = Students(25, 'Kate')
print(hash(person))






