class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res = 0
        def subseq(word1, word2):
            # word1 -> word2
            l, r = 0, 0
            while l < len(word1) and r < len(word2):
                if word2[r] == word1[l]:
                    l += 1
                r += 1
           
            return l == len(word1) 
            
        for i in range(len(strs)):
            valid = True
            for j in range(len(strs)):
                if i == j: continue
                if subseq(strs[i], strs[j]) == True:
                    valid = False
                    break
            if valid:
                res = max(res, len(strs[i]))
        return res if res > 0 else -1
