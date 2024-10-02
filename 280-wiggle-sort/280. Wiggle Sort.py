class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = sorted(nums)
        l,r = -1, -1
        if len(nums)%2==0:
            l, r = len(nums)//2 -1, len(nums)//2
        else:
            l,r = len(nums) // 2, len(nums) // 2 + 1
        idx = 0
        while idx < len(a):
            nums[idx] = a[l]
            l -= 1
            idx += 1
            if idx == len(nums): break
            nums[idx] = a[r]
            r += 1
            idx += 1
        