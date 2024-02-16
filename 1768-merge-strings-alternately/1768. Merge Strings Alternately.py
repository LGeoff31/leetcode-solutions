class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        for i in range(min(len(word1), len(word2))):
            newString += word1[i]
            newString += word2[i]
        
        newString += word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]
        return newString