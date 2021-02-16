# Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

print('Exercise 1 : What Are You Learning ?')
def display_message():
    print('I am learning about functions')

display_message()



# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.
print("=================================================")
print("Exercise 2 : What's Your Favorite Book")

def favorite_book(title):
    print(f'One of my favorite books is {title}.')

favorite_book('H is For Hawk')


# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.
print("=================================================")
print("Exercise 3 : Some Geography")

def describe_city(city, country):
    sentence = '{} is in {}'.format(city, country)
    print(sentence)

describe_city("Seattle", "Washington")


# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message to the user, otherwise show a fail message and display both numbers
print("=================================================")
import random
print('Exercise 4 : Random')
def random_number(low, high):
    print(random.randint(low, high))

random_number(1, 100)


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print("=================================================")
print("Exercise 5 : Let's Create Some Personalized Shirts !")

def make_shirt(size="large", text="I Love Python"):
    new_sentence = 'Message: {} Size: {}'.format(text, size)
    print(new_sentence)

make_shirt() 
make_shirt("small", "Happy Day")
make_shirt(size="tiny", text="Woopee")

# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.
print("=================================================")
print("Exercise 6 : Magicians")

def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())

def make_magicians_great(list_of_magicians):
    for magician in list_of_magicians:
        print(f'the Great {magician.title()}')

list_of_magicians = ['Wizard', 'Merlin', 'Marvin']
show_magicians(list_of_magicians)
make_magicians_great(list_of_magicians)


