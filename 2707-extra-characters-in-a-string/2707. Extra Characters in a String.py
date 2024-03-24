class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class Trie():
    def __init__(self, dictionary):
        self.root = TrieNode()

        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        trie = Trie(dictionary).root
        @cache
        def dfs(idx): #O(n^3)
            if idx == len(s): return 0

             #skipping character
            res = 1 + dfs(idx+1)
            #no skipping character
            curr = trie
            for i in range(idx, len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.word:
                    res = min(res, dfs(i+1))

            return res
        return dfs(0)


        