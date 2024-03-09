class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        a = nums[len(nums)-k:]
        b = nums[:len(nums)-k]
        idx = 0
        for i in range(len(a)):
            nums[idx] = a[i]
            idx += 1
        for j in range(len(b)):
            nums[idx] = b[j]
            idx += 1
        