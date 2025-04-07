'''
Collections - refers to built-in data structures that are used to
store and organise data efficiently.
Common Collections:
# 1. Lists
# 2. Tuples
# 3. Sets
# 4. Dictionaries
Specialised Collections:
# 1. namedtuple
# 2. Counter
# 3. OrderedDict
# 4. defaultdict
# 5. deque (Double-Ended Queue)
# 6. ChainMap
# 7. UserDict , UserList, UserString

Container - stores a collection of data, anything you can use the 'in' with e.g for ... in []
'''






"""
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of
position index.
"""

point = (1, 2, 3) #say this is like x,y,x then the namedtuple gives names to each one so x = 1, y = 2, z = 3
print("point x", point[0]) #This is how we would do it without namedtuple


# Now look at how namedtuple does it - we use namedtuple for things we DO NOT want mutated/changed
from collections import namedtuple

Point = namedtuple("Point", "x y z") #3 variables as we have a tuple!
# Point = namedtuple("Point", ["x", "y", "z"]) #we can use either line, 37 and 38 are the same

new_point = Point(1, 2, 3) #Assigning values to x,y,z
print(new_point.x)

#  Same thing but with Normal Dic - BUT MUTABLE
dict_point = {'x': 255, 'y': 0, 'z': 0}
print("x:", dict_point['x'])









"""
Counter is used to count the occurrences of elements in a collection, such as a list or a
string. It's essentially a specialized dictionary where elements are stored as keys,
and their counts as values. The Counter class provides a convenient and
efficient way to perform counting operations on iterable objects


It's a powerful tool for data analysis, statistics, and various scenarios where you
need to quickly determine the frequency of elements in a collection.
"""

from collections import Counter

elements = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

element_counter = Counter(elements)

print(element_counter) #print a specialised dictionary with the freq of each one
print(element_counter['a']) #prints freq of 'a' only
print(element_counter.most_common(1)) #special power, gives most common (1) - just one or (2) - gives us 2 most com


### Same thing but done using normal dictionary - usable but with the counter we get extras like most com
element_counts = {}

for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
# print("Count of 'a':", element_counts.get('a', 0))









"""
OrderedDict is a class that maintains the order of the items based on the order they
were added to the dictionary.

NOTE
Starting from Python 3.7, the standard dict type in Python also preserves the order
of insertion.

"""
from collections import OrderedDict

ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3)]) #This is the order we provide
# print(ordered_dict)
# print(ordered_dict["one"])

# You can pass a dict in as well instead of a list of tuples
another_dict = {'one': 1, 'two': 2, 'three': 3}
ordered_dict = OrderedDict(another_dict.items())
# print(ordered_dict)
# print(ordered_dict["one"])


# An interesting thing about it though
ordered_dict.move_to_end("one") #Again has extra features such as this
# print(ordered_dict)









"""
defaultdict is a subclass of the built-in dict class, and it overrides one method to
provide a default value for a nonexistent key. This makes it particularly useful when
dealing with dictionaries where you want to ensure that certain keys always have a default
value, even if they haven't been explicitly set.

NOTE!
By "override one method" it means that it overrides the __missing__ method of the
built-in dict class. The __missing__ method is called by the dict class when a key is
not found. defaultdict extends this method to provide a default value for the missing key
"""
from collections import defaultdict

# Look at this error for a normal dict
mydict = dict()
# print(mydict)
# mydict["age"] = 0  # what happens if you don't add this line before next?
# print(mydict["age"])
# mydict["age"] += 40
# print(mydict)

# instead look at this
# do above but with defaultdict

mydict = defaultdict(int)
# print(mydict)
# mydict["age"] += 40
# print(mydict)

#  REAL WORLD-ish example of usage
from collections import defaultdict

student_grades = [('Alice', 'A'), ('Charlie', 'B')]

# Create a defaultdict to store student grades with a default value of 'N/A'
grade_records = defaultdict(lambda: "Not Graded")

# Update the grades for each student
for student, grade in student_grades: #This is just normal python - student,grade = key,value works for a two item tuple
    grade_records[student] = grade

print("Grade for Alice:", grade_records['Alice'])
print("Grade for Charlie:", grade_records['Charlie'])
print("Grade for BOB:", grade_records['BOB'])









"""
A deque (pronounced "deck", like in deck of cards) in Python stands for "double-ended queue." It is a
versatile data structure that allows fast and efficient operations from both
ends — adding and removing elements from both the left and the right sides of the queue.

NOTE
We will get back to this when we're covering Stacks and Queues later
"""


from collections import deque


normal_List = [1, 2, 3, 4, 5]
# normal_List.append(6)
# print(normal_List)
normal_List.pop(0)
normal_List.insert(0, 666)
# print(normal_List)


# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])
# print("Before:", my_deque)

# Appending and popping from both ends
my_deque.append(6)          # Appending to the right
my_deque.appendleft(0)       # Appending to the left
right_pop = my_deque.pop()   # Popping from the right
left_pop = my_deque.popleft()  # Popping from the left

# print("After:", my_deque)









"""
ChainMap provides a convenient way  to manage multiple dictionaries as a single unit.
It allows you to create a chain of dictionaries and perform lookups and updates in the
order they are chained together. The dictionaries are treated as a single view,
making it easier to work with a collection of dictionaries as if they were a
merged or concatenated dictionary.
"""

from collections import ChainMap

# Imagine you're building a game with settings
default_settings = {
    "difficulty": "medium",
    "sound": "on",
    "graphics": "high"
}

# User changed some settings
user_settings = {
    "difficulty": "hard"
}

# Combine them with ChainMap (user settings take priority)
settings = ChainMap(user_settings, default_settings)

# print(settings["difficulty"])  # Outputs: "hard" (found in user_settings)
# print(settings["sound"])       # Outputs: "on" (found in default_settings)
# print(settings["graphics"])    # Outputs: "high" (found in default_settings)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

# Using dictionary unpacking operator (**)
normal_decomposition_way = {**dict1, **dict2, **dict3}
# NOTE what happens to "b" - b takes the value 3 rather than 2 bc dict2 overrides it
# print("decomposition: ", normal_decomposition_way)


# Using ChainMap
chain = ChainMap(dict1, dict2, dict3)
# print(chain)

# for key, value in chain.items():
#     print(f"{key}: {value}", end=" ")

"""
student question:
how is it different to : list = [dict1,dict2,dict3]


Answer according to the internet:
The key difference between using ChainMap and a simple list of dictionaries is that ChainMap 
provides a unified view of the dictionaries, allowing for direct lookups across all of them 
as if they were a single dictionary, while a list does not offer this behavior. 

"""









"""
UserDict provides a dictionary-like wrapper around a regular dictionary.
It's designed to make it easier to create custom dictionary-like classes by providing
a simple way to subclass and extend the behavior of dictionaries
"""
from collections import UserDict, UserList


class CustomDictionaryWithoutPop(UserDict):
    def pop(self, s=None):
        return "No Pop Today!"


a_dict = CustomDictionaryWithoutPop({"A": 666, "B": 777})


# print(a_dict)
# print(a_dict.pop("A"))
# print(a_dict)


# USER LIST

class MyUniqueList(UserList):

    def add_in_middle(self, item):
        if len(self) == 0:
            self.append(item)
        else:
            middle_index = len(self) // 2
            self[middle_index] = item


my_list = MyUniqueList([1, 2, 3, 4, 5])
print(my_list)
#
my_list.add_in_middle("CFG")
print(my_list)





