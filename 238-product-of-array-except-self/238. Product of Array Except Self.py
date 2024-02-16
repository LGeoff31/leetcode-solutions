class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        acc = 1
        for num in nums:
            acc *= num
            prefix.append(acc)
        acc = 1
        for num in nums[::-1]:
            acc *= num
            suffix.append(acc)
        suffix = suffix[::-1]
        print(prefix)
        print(suffix)
        lst = []
        for i in range(len(nums)):
            if i == 0: lst.append(suffix[i+1])
            elif i == len(nums) - 1: lst.append(prefix[len(nums)-2])
            else:
                lst.append(prefix[i-1] * suffix[i+1])
        return lst

        