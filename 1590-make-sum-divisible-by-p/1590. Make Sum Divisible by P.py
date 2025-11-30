class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:  
        """
        Try to find a subarr that has sum(subarr) % p == sum(nums) % p
        """
        currSum = 0
        targetRemainder = sum(nums) % p # 4
        if targetRemainder == 0: return 0
        dic = {0:-1}
        res = float('inf')
        for i in range(len(nums)):
            currSum = (currSum + nums[i]) % p
            looking_for = (currSum - targetRemainder) % p
            if looking_for in dic:
               idx = dic[looking_for]
               length = i-idx
               if length < len(nums):
                    res = min(res, length)
            dic[currSum] = i 
        return res if res < float('inf') else -1
