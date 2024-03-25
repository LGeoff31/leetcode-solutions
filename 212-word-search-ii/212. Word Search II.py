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
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word=True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = Trie(words).root
        res = []
        visited = set()
        # for word in words:
        #     root.addWord(word)
        
        
        
        def dfs(r,c, node, word):
            #base cases
            if r < 0 or c < 0 or r >= rows or c >= cols: return
            if (r,c) in visited: return
            if board[r][c] not in node.children: return

            #standard operations
            visited.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]

            if node.word: res.append(word)
            
            #recursion
            direction = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in direction:
                dfs(r+dr, c+dc, node, word)

            #remove
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        

        return list(set(res))


       