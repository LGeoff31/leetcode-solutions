class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
        self.indexes = []
    def addWord(self, word, i): #hghghg
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr.indexes.append(i)
            curr = curr.children[c]
        curr.indexes.append(i)
        curr.word = True
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        a = set()
        b = []
        idxSmallest = -1
        size = 1e9
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i]) < size:
                size = len(wordsContainer[i])
                idxSmallest=i
        for word in wordsContainer:
            if word not in a:
                a.add(word)
                b.append(word)
            else:
                b.append("zzzzzzzz")
        wordsContainer = b
        for i in range(len(wordsContainer)):
            wordsContainer[i] = wordsContainer[i][::-1]
        for i in range(len(wordsQuery)):
            wordsQuery[i] = wordsQuery[i][::-1]
        dic = {}
        for i, word in enumerate(wordsContainer):
            dic[word] = i
        wordsContainer = sorted(wordsContainer, key=len)
        newDic = {}
        for i in range(len(wordsContainer)):
            newDic[i] = dic[wordsContainer[i]]
        def findBestIdx(index):
            res = index[0]
            i = 1
            currSize = len(wordsContainer[res])
            while i < len(index) and currSize == len(wordsContainer[index[i]]):
                if newDic[index[i]] < newDic[res]:
                    res = index[i]
                i+=1
            return res
        lengthLst = [len(word) for word in wordsContainer]
        res = [0] * len(wordsQuery)

        root = TrieNode()
        for i in range(len(wordsContainer)):
            root.addWord(wordsContainer[i], i)

        for k, word in enumerate(wordsQuery): #O(10^4)
            curr = root
            valid = True
            for i in range(len(word)):
                if word[i] not in curr.children and i == 0: 
                    res[k] = idxSmallest
                    break
                else:
                    if word[i] not in curr.children:
                        valid=False
                        z = findBestIdx(curr.indexes)
                        res[k] = newDic[z]
                        break
                    else:
                        curr = curr.children[word[i]]
            if valid: 
                z = findBestIdx(curr.indexes)
                res[k] = newDic[z]
        return res
       