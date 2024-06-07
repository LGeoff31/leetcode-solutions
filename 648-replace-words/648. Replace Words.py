class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def add(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.endWord = True


    def prefix(self, word):
        cur = self.root
        for i, letter in enumerate(word):
            if cur.endWord:
                return word[:i]
            elif letter not in cur.children:
                return word
            else:
                cur = cur.children[letter]
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        res = []
        for word in sentence.split():
            res.append(trie.prefix(word))
        return " ".join(res)

        