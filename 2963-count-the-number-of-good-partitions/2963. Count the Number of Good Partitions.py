class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        first, last = {}, {}

        for i, num in enumerate(nums):
            if num in first:
                last[num] = i
            else:
                first[num] = i
                last[num] = i

        MOD = 10 ** 9 + 7
        count = -1
        farthest = -1
        for i in range(len(nums)):
            if i > farthest: #start new partition
                count += 1
            farthest = max(farthest, last[nums[i]])

        return 2 ** (count) % MOD
        