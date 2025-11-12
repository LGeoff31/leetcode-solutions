class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 1e9
        if 1 in nums:
            return sum(1 for n in nums if n != 1)
        def calc(subarr):
            curr = gcd(subarr[0], subarr[1])
            for i in range(2, len(subarr)):
                curr = gcd(curr, subarr[i])
            return curr
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                subarr = nums[i:j+1]
                if len(subarr) >= 2 and calc(subarr) == 1:
                    res = min(res, len(subarr))
        print(res)
        return len(nums) + res - 2 if res != 1e9 else -1