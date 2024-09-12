class MagicDictionary:
    def __init__(self):
        self.lst = []
        

    def buildDict(self, dictionary: List[str]) -> None: #O(n), n is amount of words
        self.lst = dictionary
    
    def isMatch(self, word1, word2): #O(m), where m is max(len(word1), len(word2))
        differences = 0
        if len(word1) != len(word2):
            return False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differences += 1
        return differences == 1

    def search(self, searchWord: str) -> bool: #O(nm)
        for word in self.lst:
            if self.isMatch(searchWord, word):
                return True 
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)