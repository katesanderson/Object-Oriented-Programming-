'''

A function which references and calls itself in its own body code
Recursionvisualizer.com helps!!

# When To Recursion
#### This is not as easy as just giving you a list. It will take some time and experience for you to get your head around WHEN to recursion. But I do promise it will come to you eventually!

1. The problem can be broken into smaller, similar sub-problems:
    * For example, calculating factorial (n!) or finding Fibonacci numbers. These naturally follow a divide-and-conquer
      pattern (Note that we haven't yet covered this, but its easy to google).

2. The problem has a natural "stop condition":
    * For example, summing numbers until 0 or reversing a string until it’s empty.

3. Tree-like (or graph-like) structures need to be explored:
    * For example, searching in hierarchical data like file directories or binary trees. Recursion is cleaner for these
      cases.

4. You want simpler, more readable code for specific tasks:
    * Recursion can often make the logic clearer compared to a loop, especially for problems with unknown or dynamic
      depth (e.g., navigating a maze).

### However, avoid recursion if:

1. The problem is easily handled with a loop (e.g., counting numbers in a range).
2. There’s a risk of hitting recursion depth limits (too many levels).

'''






#Example 1 - basic to help understand
def chest_quest(level):
    #print(level)

    if level == -3: #base case
        return "Treasure" # Where does this return go? - levels us one back - only one!

    return chest_quest(level - 1) #Putting the return here gets us out

#print(chest_quest(0))
#Getting recursion to stop - base case - the recursion stops but we need to get out!








#Example 2
def recursive_adder(num):

    if num == 0:
        return 0 #3+(2+(1+0))

    return num + recursive_adder(num - 1)

#print(recursive_adder(3))






#Example 3
def walk(step):
    #print(step)

    if step == 10:
        return

    return walk(step + 1)


#print(walk(0))








#Example 4
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


print(factorial(3))































