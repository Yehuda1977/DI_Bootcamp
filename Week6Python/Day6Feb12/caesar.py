def caesar_cypher(text):
    cypher_text = ''
    for letter in text:
        cypher_text += chr(ord(letter) + 3)
    return cypher_text

text = input('Enter a text')
print(caesar_cypher(text))