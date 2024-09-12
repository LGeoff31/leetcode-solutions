class TrieNode:
    def __init__(self):
        self.endWord = False 
        self.children = {}

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endWord = True

    def buildDict(self, dictionary: List[str]) -> None: 
        for word in dictionary:
            self.insertWord(word)
    
    def search(self, searchWord: str) -> bool:
        curr = self.root

        def dfs(node, i, differences):
            # If there's a mismatch, increment differences by 1 and auto go to correct one
            if i == len(searchWord):
                return differences == 1 and node.endWord
            if differences > 1:
                return False 

            if searchWord[i] in node.children:
                if dfs(node.children[searchWord[i]], i + 1, differences):
                    return True

            for child in node.children:
                if child != searchWord[i]:
                    if dfs(node.children[child], i+1, differences + 1):
                        return True
            return False

        return dfs(curr, 0, 0)
        

        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)