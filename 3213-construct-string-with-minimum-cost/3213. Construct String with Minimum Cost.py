class Node:
    def __init__(self):
        self.children = {}
        self.endWord = False
        self.cost = 1e9


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = Node()
        # Create the Trie
        for i in range(len(words)):
            node = trie
            for c in words[i]:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.cost = min(node.cost, costs[i])
            node.endWord = True
        
        @cache
        def dfs(i):
            if i >= len(target):
                return 0
            res = 1e9
            node = trie
            for idx in range(i, len(target)):
                c = target[idx]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.endWord:
                    res = min(res, node.cost + dfs(idx+1))
            return res
        res = dfs(0)
        dfs.cache_clear()
        return res if res != 1e9 else -1
