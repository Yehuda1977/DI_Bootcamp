def caesar_cypher(text):
    cypher_text = ''
    for letter in text:
        if letter == 'Z':
            cypher_text += 'C'
        elif letter == 'z':
            cypher_text += 'c'
        elif letter == ' ':
            cypher_text += ' '
        
        else:
            cypher_text += chr(ord(letter) + 3)
    return cypher_text



text = input('Enter a text: ')
print(caesar_cypher(text))


