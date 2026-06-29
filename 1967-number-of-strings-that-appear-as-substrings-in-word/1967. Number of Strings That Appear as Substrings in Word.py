class Trie:
    def __init__(self):
        self.parent = {}
    
    def insert(self, word):
        curr = self.parent
        for c in word:
            if c not in curr:
                curr[c] = Trie()
            curr = curr[c].parent
        
    def find(self, word):
        curr = self.parent
        for c in word:
            if c not in curr:
                return False
            curr = curr[c].parent
        return True
        
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(w in word for w in patterns)
        

