class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
        self.val = []
        self.counter = 0
    
    def addWord(self, word, solution):
        curr = self
        for i in range(len(word)):
            if (word[i], word[len(word) - i - 1]) not in curr.children:
                curr.children[(word[i], word[len(word) - i - 1])] = TrieNode() 
            curr = curr.children[(word[i], word[len(word) - i - 1])]
            # if curr.word and i == len(word)-1: 
            #     curr.counter+=1
            #     print('reached')
            #     solution.res+=curr.counter
            if curr.word:
                solution.res+=curr.counter
        curr.word=True
        curr.counter+=1

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        self.res = 0
        root = TrieNode()

        for word in words:
            root.addWord(word, self)
            print('added')

        return self.res
        

        