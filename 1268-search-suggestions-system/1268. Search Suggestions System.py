class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        for product in products:
            curr = root

            for c in product:
                if c not in curr.children:
                    curr.children[c] = TrieNode()

                curr = curr.children[c]

                curr.suggestions.append(product)
                curr.suggestions.sort()
                if len(curr.suggestions) > 3:
                    curr.suggestions.pop()

        curr = root
        suggested = []
        
        for c in searchWord:
            if c in curr.children:
                curr = curr.children[c]
                suggested.append(curr.suggestions)

            else:
                curr.children = {}
                suggested.append([])

        return suggested


            

