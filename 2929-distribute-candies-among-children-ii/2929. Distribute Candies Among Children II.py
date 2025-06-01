class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # How many size-3 tuples sum to n
        # How many size-3 tuples sum to n, where each of the three values <= limit
        # @cache
        # def dfs(currSum, size): # O(3n * limit)
        #     if size == 3:
        #         return 1 if currSum == n else 0
        #     total = 0
        #     for i in range(limit+1):
        #         total += dfs(currSum + i, size + 1)
        #     return total
        
        # Combinatorics question instead of recursion/dp question????
        # res = 0
        # for i in range(limit):
        #     a = i
        #     b = -1
        #     c = -1
        #     if n-a >= 0:
        #         b = n-a+1
        #     if n-a-b >= 0:
        #         c = n-a-b+1
        # return a*b*c
        res = 0
        for i in range(min(limit, n) + 1): # 0,1,2,3
            target_sum = n - i
            # We want to pick a j value, such that there will exist a k value, j+k = n-i. 0<=k<=limit, 0<=j<=limiit
            if target_sum <= limit:
                res += min(limit,target_sum)+1
            else:
                res += max(limit - (target_sum - limit) + 1,0)
            # print(res)
        return res

        # return dfs(0, 0)//