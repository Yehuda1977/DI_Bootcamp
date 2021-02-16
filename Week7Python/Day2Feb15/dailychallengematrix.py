# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:

#     7i3
#     Tsi
#     h%x
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!

def read_matrix(matrix):
    # the matrix of arrays is reformatted based on reading each column from top to bottom,
    # one new array is created that contains all the characters
    # a while loop is used to control which index of the array is being added in the for loop
    columns = []
    index = 0
    while index < 3:
        for element in matrix:
            columns.append(element[index])
        index += 1
    
    decoded_matrix = ''
   
    for char in columns:
         # Only alphabetic characters are added to the decoded_matrix
        if char.isalpha():
            decoded_matrix += char   
        # Non alphabetic characters are replaced with a space  
        else:
            decoded_matrix += ' '
    
    # In order to remove extra whitespace the decoded_matrix string is split into
    # an array of words and then joined again with only one space
    decoded_matrix = ' '.join(decoded_matrix.split())
        
    print(columns)
    print(decoded_matrix)


matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]   

read_matrix(matrix)