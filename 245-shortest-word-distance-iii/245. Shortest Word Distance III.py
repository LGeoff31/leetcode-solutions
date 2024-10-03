class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lst1 = []
        lst2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                lst1.append(i)
            elif wordsDict[i] == word2:
                lst2.append(i)
        res = 1e9
        if word1 == word2:
            for i in range(len(lst1) - 1):
                res = min(res, lst1[i+1]-lst1[i])
            return res
        print(lst1)
        print(lst2)
        # Assuming word1 != word2
        for idx in lst1:
            res = min(res, abs(idx - lst2[bisect.bisect_left(lst2, idx) - 1]))
        for idx in lst2:
            res = min(res, abs(idx - lst1[bisect.bisect_left(lst1, idx) - 1]))

        return res
        

        # a: [0, 3]
        # b: [2]