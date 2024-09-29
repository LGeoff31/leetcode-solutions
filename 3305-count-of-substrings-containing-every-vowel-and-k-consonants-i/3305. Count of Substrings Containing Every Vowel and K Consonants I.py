class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        def valid(string):
            for key in vowels:
                if key not in string:
                    return False 
            consonant = 0
            for w in string:
                if w not in vowels:
                    consonant += 1
            return consonant == k
        res = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                substring = word[i:j+1]
                if valid(substring):
                    res += 1
        return res            
    