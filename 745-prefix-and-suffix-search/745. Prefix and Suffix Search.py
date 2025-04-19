"""
Simplify the problem, assume you just wanted the prefix to match.
Put all the words into a Trie (prefix-tree).
When we get the prefix, we just need to go through Trie, 
1. Ensure that all elements of prefix can be scooped up
2. If so, it's possible there may be multiple words, traverse all those words and ensure the last node for the word has lastCharacter=True alongside index=x
3. That way we should pick the largest valid word containg that prefix

O(max(length of a word)) rather than having to iterate over all the words in dictionary


Now add on to this idea by introducint a suffix tree, now both conditions must be met
Find indicies where prefix-tree valid, find indicies where suffix-tree valid, find the largest index within the intersection between the two
"""

class PrefixNode:
    def __init__(self):
        self.endWord = False
        self.idx = -1
        self.children = {}

class SuffixNode:
    def __init__(self):
        self.endWord = False
        self.idx = -1
        self.children = {}

class WordFilter:
    def __init__(self, words: List[str]):
        self.prefixTree = PrefixNode()
        self.suffixTree = SuffixNode()     
        for i, word in enumerate(words):
            self.insertPrefixWord(word, i)
            self.insertSuffixWord(word[::-1], i) # NOTE: this can be precomputed

    def insertPrefixWord(self, word, idx):
        curr = self.prefixTree
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixNode()
            curr = curr.children[c]

        curr.endWord=True
        curr.idx = idx
    
    def insertSuffixWord(self, word, idx):
        curr = self.suffixTree
        for c in word:
            if c not in curr.children:
                curr.children[c] = SuffixNode()
            curr = curr.children[c]

        curr.endWord=True
        curr.idx = idx
    
    def dfs(self, currPrefix, indicies):
        if currPrefix.endWord:
            indicies.add(currPrefix.idx)
        for key in currPrefix.children.values():
            self.dfs(key, indicies)

    def f(self, pref: str, suff: str) -> int: # O(n * (a+b))
        suff = suff[::-1]
        currPrefix = self.prefixTree
        currSuffix = self.suffixTree

        # Ensure all prefix is satisfied
        for c in pref:
            if c in currPrefix.children:
                currPrefix = currPrefix.children[c]
            else:
                return -1
        # DFS to find all the words that had that prefix
        indicies = set()
        self.dfs(currPrefix, indicies) 

        # Ensure all prefix is satisfied
        for c in suff:
            if c in currSuffix.children:
                currSuffix = currSuffix.children[c]
            else:
                return -1
        # DFS to find all the words that had that suffix
        indicies2 = set()
        self.dfs(currSuffix, indicies2) 
        cands = indicies & indicies2
        return max(cands) if cands else -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)