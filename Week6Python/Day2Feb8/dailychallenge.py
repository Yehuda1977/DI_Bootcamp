# 1. Using the input function, ask the user for a string. The string must be 10 characters long.
#     If it’s less than 10 characters, print a message which states “string not long enough”
#     If it’s more than 10 characters, print a message which states “string too long”
# 2. Then, print the first and last characters of the given text
# 3. Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
#     Example:
#         The user enters “Hello Word”
#         Then, you have to construct the string character by character
#         H
#         He
#         Hel
#         … etc
#         Hello World
# 4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
#     Example:
#         Hlrolelwod
import random

string = input('Please enter a string: ')
if len(string) < 10:
    print(f'The string "{string}" is not long enough')
elif len(string) > 10:
    print(f'The string "{string}" is too long')
print(string[0], string[-1])


index = 1
while index <= len(string):
    print(string[0:index])
    index += index
print(string)

string_array = [char for char in string]
random.shuffle(string_array)

shuffled_string = ''

for char in string_array:
    shuffled_string += char
print(shuffled_string)

