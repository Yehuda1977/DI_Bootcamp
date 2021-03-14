from anagram_checker import AnagramChecker as anchecker

ana = anchecker()

def show_menu():
    print('\nChoose from the following menu:')
    print('\n   [A] Find the anagram(s) of a word.')
    print('\n   [any other key] Exit\n')
    selection = input('What is your selection: ').lower()
    if selection == 'a':
        return True
    else:
        return False
    

def main():
    while show_menu():
        word = input('\nWhat word would you like to find the anagram(s) for? ')
        word = word.strip()
        if word.isalpha():
            if ana.is_valid_word(word):
                print(f'\n{word.upper()} is a valid English word.')
                if len(ana.get_anagrams(word)) > 1:
                    print('\nAnagram(s) for your word:\n')
                    print(', '.join(ana.get_anagrams(word)))
                else:
                    print(f'\nNo anagrams have been found for {word.upper()}.\n')
            else:
                print(f'\n{word.upper()} is NOT a valid English word.\n')
        else:
            print('\nNot a valid word. Please try again.\n')
main()


# print(ana.is_anagram('cat', 'tcb'))
# print(ana.get_anagrams('meat'))