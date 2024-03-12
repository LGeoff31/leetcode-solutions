class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            if num not in a:
                a.append(num)
        for i in range(len(a)):
            nums[i] = a[i]

        return len(a)
        