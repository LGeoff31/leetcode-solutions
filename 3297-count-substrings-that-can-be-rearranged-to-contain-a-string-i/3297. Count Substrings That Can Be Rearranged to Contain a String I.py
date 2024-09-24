class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        l, r = 0, 0
        res = 0
        a = Counter(word2)
        def is_valid(dic):
            for key in a:
                if key not in dic:
                    return False 
                if dic[key] < a[key]:
                    return False 
            return True 
        dic = {word1[0] : 1}
        while r < len(word1):
            # Move right until valid string
            while not is_valid(dic):
                r += 1
                if r == len(word1): break
                dic[word1[r]] = 1 + dic.get(word1[r], 0)
            res += len(word1) - r 
            while is_valid(dic):
                dic[word1[l]] -= 1
                if dic[word1[l]] == 0:
                    del dic[word1[l]]
                l += 1
                if is_valid(dic):
                    res += len(word1) - r 
            r += 1
            if r >= len(word1): break
            dic[word1[r]] = 1 + dic.get(word1[r], 0)
            print(l, r, res)
        return res