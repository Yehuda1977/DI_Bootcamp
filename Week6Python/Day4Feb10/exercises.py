# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

my_fav_numbers = [21, 22, 23, 24, 25, 26, 27, 28]
my_fav_numbers = my_fav_numbers + [4,7]
my_fav_numbers.pop(-1)
print(my_fav_numbers)