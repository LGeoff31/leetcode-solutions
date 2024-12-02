class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if searchWord in word[:len(searchWord)]:
                return i+1      
        return -1