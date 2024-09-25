class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.freq += 1
    def evaluate(self, word):
        res = 0
        curr = self.root
        for c in word:
            curr = curr.children[c]
            res += curr.freq
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = [0] * len(words)
        trie = Trie()
        for word in words:
            trie.addWord(word)
        for i in range(len(words)):
            res[i] = trie.evaluate(words[i])
        return res



        