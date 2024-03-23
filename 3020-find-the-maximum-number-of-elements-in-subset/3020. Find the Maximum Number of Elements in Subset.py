class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        if nums.count(1) == 2 and len(nums) > 2: res+=2
        oneCount = nums.count(1)
        if oneCount %2==0: oneCount-=1
        unique = set(nums)
        for num in unique:
            if num > 1 and num*num in unique and nums.count(num) > 1:
                count = 1
                while num*num in unique:
                    count+=2
                    num=num*num
                    if nums.count(num) == 1:break
                res=max(res, count)
        return max(1,res, oneCount)




        