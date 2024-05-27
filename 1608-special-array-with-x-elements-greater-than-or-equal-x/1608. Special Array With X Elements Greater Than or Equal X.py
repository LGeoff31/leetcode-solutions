class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1, n+1):
            if n - bisect.bisect_left(nums, i) == i:
                return i
        return -1
        
        #[0,0,3,4,4]