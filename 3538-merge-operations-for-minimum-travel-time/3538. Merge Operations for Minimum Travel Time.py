class Solution:
    def minTravelTime(self, l: int, n: int, k: int, pos: List[int], time: List[int]) -> int:
        pos.append(l)
        @cache
        def dp(i, k, t):
            if i + k >= n:
                return inf
            if i == n-1:
                return 0
            p = pos[i]
            ans = t * (pos[i+1] - pos[i]) + dp(i+1, k, time[i+1])
            cost = 0
            for m in range(k+1):
                j = i+m+1
                if j >= n:
                    break
                cost += time[j]
                ans1 = t * (pos[j] - pos[i]) + dp(j, k-m, cost)
                ans = min(ans, ans1)
            return ans
        return dp(0, k, time[0])