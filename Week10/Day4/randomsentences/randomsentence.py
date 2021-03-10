import random
words = []

def get_words_from_file():
    
    with open("sowpods.txt", encoding = 'utf-8') as f:
        for i in f:
            words.append(i.rstrip("\n"))


def get_random_sentence(length):
    count = length
    num_of_words = len(words)
    sentence = []
    while count > 0:
        index = random.randint(0, num_of_words)
        sentence.append(words[index])
        count -= 1
    # print(sentence)
    clean_sentence = ''
    clean_sentence += sentence[0].title()
    for i in range(1, length):
        clean_sentence += ' ' + sentence[i].lower()
    clean_sentence += '.'
    print(clean_sentence)

# get_words_from_file()
# get_random_sentence(7)

def main():
    print('This program will generate random sentences.')
    length = input('How many words do you want in your sentence?')
    get_words_from_file()
    get_random_sentence(int(length))

main()