class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def product(arr):
            res = 1
            for num in arr:
                res *= num
            return res
        def gcd1(arr):
            result = arr[0]
            for num in arr[1:]:
                result = gcd(result, num)
            return result
        def lcm1(arr):
            result = arr[0]
            for num in arr[1:]:
                result = lcm(result, num)
            return result
        # def lcm1(arr):
        #     return abs(a * b) // gcd(a, b)
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i:j+1]
                if product(subarr) == gcd1(subarr) * lcm1(subarr):
                    res = max(res, len(subarr))
        return res
                