def reverse_integer(num):
    n = str(num)
    if n[0] == '-':
        return int('-'+n[:0:-1])
    return int(n[::-1])

#print(reverse_integer(-147))  # ➝ -741
#print(reverse_integer(852))   # ➝ 258


from collections import Counter

def average_word_length(word):
    for p in '!.,/?-_+=><':
        word = word.replace(p,'')

    words = word.split()
    hold = []
    for w in words:
        hold.append(len(w))
    total = 0
    for i in hold:
        total = total + i

    print(round(total/len(hold)))





# average_word_length('Hello! My Name is Kate')
#average_word_length("Hi class, we are practicing solving algorithms. It is fun, don't you think?..")
# average_word_length("We need to work very hard to learn more about algorithms!")

def add_strings(num1,num2): #Without turning to integers
    n1 = n2 = 0
    for i in num1:
        n1 = n1 * 10 + (ord(i)- ord('0'))
    for k in num2:
        n2 = n2 * 10 + (ord(k)- ord('0'))#ASCII numbers

    print(n2 + n1)

#add_strings('257', '2754')


def first_unique(word):
    letters = Counter(word)
    com = letters.most_common(1)
    print(com[0][0])

#first_unique('aabccbdcbe')


def is_monotonic(lst):
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False

    return increasing or decreasing




print(is_monotonic([100, 6, 5, 4, 4]))     # ➝ True
print(is_monotonic([1, 1, 1, 3, 3, 4]))    # ➝ True
print(is_monotonic([1, 2, 3, 7, 11, 22]))  # ➝ True
print(is_monotonic([100, 99, 101, 97, 200]))








