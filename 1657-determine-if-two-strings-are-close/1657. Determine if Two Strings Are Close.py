class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): #O(n + m)
            return False
        preprocessing_letters_word2 = set()
        for char in word2: #O(m)
            preprocessing_letters_word2.add(char)

        for char in word1: #O(n)
            if char not in preprocessing_letters_word2:
                return False
        a = []  
        visited1 = set() 
        for char in word1: #O(n)
            if char not in visited1:
                visited1.add(char)
                a.append(word1.count(char)) #O(m)
        
        b = []
        visited2 = set()
        for char in word2:
            if char not in visited2:
                visited2.add(char)
                b.append(word2.count(char))

        a.sort()
        b.sort()
        print(a)
        print(b)
        if a==b:
            return True
        return False
            
        
        