class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        a,b,c = 0,0,0

        def calc(arr):
            res = 0
            for i in range(len(prices)):
                res += prices[i] * arr[i]
            return res
        # sliding window?
        
        n = len(strategy)
        base = calc(strategy)
        # for i in range(floor(k/2)):
        #     new_b[i] = 0
        #     new_c[n-i-1] = 1
        h = k // 2
        A, B = [-strategy[i] * prices[i] for i in range(n)], [(1-strategy[i]) * prices[i] for i in range(n)]
        pA, pB = [0] * (n+1), [0] * (n+1)
        for i in range(n):
            pA[i+1] = pA[i] + A[i]
            pB[i+1] = pB[i] + B[i]
        res = 0
        for i in range(n-k+1):
            first = pA[i+h] - pA[i]
            second = pB[i+k] - pB[i+h]
            d = first + second
            res = max(d, res)
    
        return base + res