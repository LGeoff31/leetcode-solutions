class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom, cnt = max(Counter(nums).items(), key = lambda x: x[1])
        left, cut = 0, 2*cnt - len(nums)

        if cut < 2: return -1

        for i, num in enumerate(nums):

            left+= 2*(num == dom)
            if 1 < left - i <= cut: return i