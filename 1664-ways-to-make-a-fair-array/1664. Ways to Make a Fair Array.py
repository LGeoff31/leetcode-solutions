class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        odd = 0
        even = 0

        oddSum = sum(nums[i] for i in range(len(nums)) if i%2==0)
        evenSum = sum(nums[i] for i in range(len(nums)) if i%2==1)

        for i in range(len(nums)):
            if i%2==0: #ood
                odd += nums[i]
                newEven = even +  oddSum - odd
                newOdd = odd + evenSum - even - nums[i]
                if newOdd == newEven: res+=1
            else:
                even += nums[i]
                newEven = even +  oddSum - odd - nums[i]
                newOdd = odd + evenSum - even
                if newOdd == newEven: res+=1
        print(oddSum, evenSum)
        return res

        