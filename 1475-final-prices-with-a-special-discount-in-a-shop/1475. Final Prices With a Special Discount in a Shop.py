class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # (idx, val) -> increasing order
        ans = [0] * len(prices)
        for i, num in enumerate(prices):
            while stack and num <= stack[-1][1]:
                idx, val = stack.pop()
                ans[idx] = val - num
            stack.append((i, num))
        while stack:
            idx, val = stack.pop()
            ans[idx] = val
        return ans



# [8, 4]

# []


# [(3,2), (4,3)]
# [4, 2, 4, 0, 0]