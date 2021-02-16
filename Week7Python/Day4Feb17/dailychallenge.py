# Write a function to compute 5/0 and use try/except to catch the exceptions.

def division(a, b):
    total = 0
    try:
        total = a / b
        return total
    except:
        print('You cannot divide by zero')
    

print(division(5,0))