class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # key ideas 1.) Every value is distinct 2.) Two groups sorted Arrays
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
