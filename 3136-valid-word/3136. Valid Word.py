class Solution:
    def isValid(self, word: str) -> bool:
        vowel = consonant = False
        for c in word:
            if c.isdigit():
                continue
            elif c.isalpha():
                if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                    vowel = True
                else:
                    consonant = True
                continue
            else:
                return False
        return vowel and consonant and len(word) >= 3
        
        