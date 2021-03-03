# Exercise 1 : Built-In Functions
# Python has many built-in functions, and if you do not know how to use it, you can read document online.
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function

def print_docs(function):
    documents = eval(function + '.__doc__')
    return documents
    
function = input('Which function do you want documentation for?')

print(print_docs(function))

# Exercise 2: Currencies
# Recreate these results
# Hint : When you add 2 currencies, if they don’t have the same label raise an error
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency():
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value
    def __str__(self):
        return self.kind
    # def __int__(self):
    #     return self.value
    def __add__(self, other):
        if isinstance(other, Currency):
            return self.value + other.value
        else:
            return self.value + other 
    def __iadd__(self, other):
        self.value = self.value + other
        return self.value
    def __repr__(self):
        return str(self.value)

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
# print(str(c1))
# print(int(c1))

# print(int(c1))
# sum = c1 + 1
# print(sum)
# c1 += 5
# print(c1)



