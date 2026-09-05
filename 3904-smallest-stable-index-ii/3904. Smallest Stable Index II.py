class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        largest_prefix = []
        smallest_suffix = []

        curr = 0
        for n in nums:
            curr = max(curr, n)
            largest_prefix.append(curr)

        curr = 1e9
        for n in nums[::-1]:
            curr = min(curr, n)
            smallest_suffix.append(curr)
        smallest_suffix = smallest_suffix[::-1]

        for i in range(len(nums)):
            if largest_prefix[i] - smallest_suffix[i] <= k:
                return i
        return -1