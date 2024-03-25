class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        res = []
        visited = set()
        for word in words:
            root.addWord(word)
        
        
        def dfs(r,c, node, word):
            #nase cases
            if r < 0 or c < 0 or r >= rows or c >= cols: return
            if (r,c) in visited: return
            if board[r][c] not in node.children: return

            #standard operations
            visited.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]

            if node.word: res.append(word)

            #recursion
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            #remove
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        

        return list(set(res))


       