class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        dic = Counter(candies)
        l, r = 0, k - 1
        # Initialize window
        for i in range(l, r+1):
            dic[candies[i]] -= 1
            if dic[candies[i]] == 0:
                del dic[candies[i]]
        
        res = len(dic)
        # print(dic)
        while r < len(candies):
            r += 1
            if r == len(candies): break
            dic[candies[r]] -= 1
            if dic[candies[r]] == 0:
                del dic[candies[r]]
            dic[candies[l]] += 1
            l += 1
            # print(dic)
            res = max(res, len(dic))
        return res
