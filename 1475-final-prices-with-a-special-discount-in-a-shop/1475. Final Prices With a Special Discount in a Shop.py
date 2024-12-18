class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # (idx, val) -> increasing order
        ans = [0] * len(prices)
        for i, num in enumerate(prices):
            while stack and num <= stack[-1][1]:
                idx, val = stack.pop()
                ans[idx] = val - num
            stack.append((i, num))
        # Remains which don't have any discounts
        while stack:
            idx, val = stack.pop()
            ans[idx] = val
        return ans