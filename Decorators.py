'''
A decorator is a function that takes one fucntion as an input and
returns another function

GET, POST are some examples of decorators

A Base function is the function you pass into the decorator

Keep decorators in a separate file and import them

Can use multiple decorators - chained decorators, closest to function is applied first



'''

#Example 1
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_hello():
    print("Hello!!")

#decorated_function = my_decorator(say_hello)
#decorated_function()



#Example 2
def square_it(func):
    def wrapper(*args): #*args is argument
        result = func(*args)
        print(result*result)
    return wrapper

@square_it
def add_two_nums(a,b):
    return a + b


@square_it
def add_three_nums(a,b,c):
    return a + b + c

#add_two_nums(2,3)
#add_three_nums(2,3,1)



#Example 3 - using args
def create_profile(name, age, **kwargs): #**kwargs is key word argument
    profile = {
        "name": name,
        "age": age
    }
    profile.update(kwargs)
    return profile


#user = create_profile("Alice", 30, location="New York", job="Engineer")
#print(user)



#Example 4
import time

def timer(func):
    def inner_wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished in {end - start:.8} secs")
        return value
    return inner_wrapper


@timer
def slow_function(n):
    return sum(i for i in range(n))

print(slow_function(10))



#Example 5

class MemorizeDecorator:
    def __init__(self, function):
        self.cache = {} #to store results
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs) #use input as a unique key
        if key in self.cache:
            print("Using cached result.")
            return self.cache[key]  #return saved values
        result = self.function(*args, **kwargs)
        self.cache[key] = result    #save result
        return result


@MemorizeDecorator
def compute(num):
    return sum(i*i for i in range(num))


print(compute(100))
print("Second time: - ")
print(compute(100))
