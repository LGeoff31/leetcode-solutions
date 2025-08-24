class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        return len(nums) % k == 0 and max(Counter(nums).values()) <= (len(nums) // k)