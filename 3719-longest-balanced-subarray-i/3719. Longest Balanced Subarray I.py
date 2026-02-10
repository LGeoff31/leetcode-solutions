class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        def valid(subarr):
            a = set(subarr)
            even, odd = sum(1 for c in a if c % 2 == 0), sum(1 for c in a if c % 2 == 1)
            return even == odd
        res = 0
        for i in range(len(nums)):
            lst = []
            seen = set()
            even, odd = 0, 0
            for j in range(i, len(nums)):
                lst.append(nums[j])
                if nums[j] not in seen:
                    even += nums[j] % 2 == 0
                    odd += nums[j] % 2 == 1

                seen.add(nums[j])
                if even == odd:
                    res = max(res, len(lst))
        return res