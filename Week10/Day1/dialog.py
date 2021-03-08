import operations

print("Welcome to our special calculator where no result is under 0")
print("Choose an operation:")
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")



user_choice = input("> ") # a, b, c, or d

number1 = int(input("Please give me a number: "))
number2 = int(input("Please give me another number: "))

if user_choice == 'a':
    print(operations.add(number1, number2))
if user_choice == 'b':
    print(operations.subtract(number1, number2))
if user_choice == 'c':
    print(operations.multiply(number1, number2))
if user_choice == 'd':
    print(operations.divide(number1, number2))