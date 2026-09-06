class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def is_bigger(word2, word1):    
            print(word2, word1)
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if order.index(word1[i]) > order.index(word2[i]):
                        return False 
                    else:
                        return True
            return len(word2) >= len(word1)

        for i in range(1, len(words)):
            if not(is_bigger(words[i], words[i-1])):
                return False 
        return True