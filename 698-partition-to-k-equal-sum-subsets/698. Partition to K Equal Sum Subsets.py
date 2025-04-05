class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False 
        target = sum(nums) // k
        nums.sort(reverse=True)
        buckets = [0] * k
        # @cache
        def backtrack(idx):
            if idx == len(nums):
                return all(num == target for num in buckets)

            for i in range(len(buckets)):
                if nums[idx] + buckets[i] <= target:
                    found = True
                    buckets[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    buckets[i] -= nums[idx]
                    if buckets[i] == 0: break

            return all(num == target for num in buckets)
        ans = backtrack(0)
        return ans
        