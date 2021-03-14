class AnagramChecker():
    anagram_list = []
    def __init__(self):
        file = open('sowpods.txt', "r")
        f = file.read()
        self.word_list = f.lower().split('\n')
        file.close()
           
    def is_valid_word(self, word):
        return True if word in self.word_list else False


    def is_anagram(self, word1, word2):
        w1 = list(word1)
        w2 = list(word2)
        if len(w1) == len(w2):
            while w1:
                if w1[0] in w2:
                    w2.remove(w1[0])
                    w1.pop(0)   
                else:
                    return False
        else:
            return False
        return True
    
    def get_anagrams(self, word):
        self.anagram_list.clear()
        if self.is_valid_word(word):
            for entry in self.word_list:
                if self.is_anagram(entry, word):
                    self.anagram_list.append(entry)
                else:
                    continue
            return self.anagram_list
        else:
            return None





 