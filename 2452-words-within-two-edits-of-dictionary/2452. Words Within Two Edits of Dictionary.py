class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def match(word1, word2):
            if len(word1) != len(word2):
                return False 
            
            diff = 0
            for i in range(len(word1)):
                diff += word1[i] != word2[i]
            return diff <= 2
        res = []
        visited = set()
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                if match(queries[i], dictionary[j]):
                    res.append(queries[i])
                    break
        return res
        