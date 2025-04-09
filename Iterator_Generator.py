# Iterators are objects allow to traverse through a collection, a stream of data which is iterable, returns one at a time
# __iter__ - returns the iterator object itself
# __next__ - returns the next value from the sequence or stop if there are no more items
# StopIteration when there are no more items
# Iterators remember where you are in the loop
# Generator are also iterators but uses yield instead of return, it automatically creates an iterator, a simple way of creating iterators
# more elegant than iterators - uses yield
# __init__ __iter__ __next__
#
# Generator is always an Iterator
# Iterator is not always a Generator
#

#Example 1
nums = [1,2,3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))


#Example 2
class EvenNumbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num < 10:
            self.num += 2
            return self.num
        else:
            raise StopIteration

evens = EvenNumbers()
even_iter = iter(evens) #Here we use the built-in iter function on the object evens which is an instance fo the EvenNumbers class

print(next(even_iter))
print(next(even_iter))
print(next(even_iter))


#Example 3
class PowerThreeSequence:
    def __init__(self, max_items = 0):
        self.n = 0
        self.max = max_items

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        result = 3 ** self.n
        self.n += 1
        return result

my_iter = PowerThreeSequence(5)
for i in my_iter:
    print(i)

 #Example 3 using generator - see it is much simpler
def power_three(max_items = 0):
    n = 0
    while n < max_items:
        yield 3 ** n
        n += 1

my_gen = power_three(5)
for i in my_gen:
    print(i)


#Example 4
def countdown(n):
    while n>0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)



