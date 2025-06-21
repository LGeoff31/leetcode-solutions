class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dic = Counter(word)
        res = 1e9
        print(dic)
        for k1 in dic:
            target = dic[k1] # smallest
            curr = 0
            for k2 in dic:
                if dic[k2] < target:
                    curr += dic[k2]
                elif abs(dic[k2] - target) > k:
                    curr += abs(dic[k2] - target) - k
            res = min(res, curr)
          
        return res
