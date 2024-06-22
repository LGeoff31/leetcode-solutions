class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        amountOdd = 0
        res = 0
        dic = {}

        for i in range(len(nums)):
            amountOdd += nums[i] % 2 == 1
            if amountOdd == k:
                res += 1
            if amountOdd - k in dic:
                res += dic[amountOdd - k]
            dic[amountOdd] = 1 + dic.get(amountOdd, 0)
        return res