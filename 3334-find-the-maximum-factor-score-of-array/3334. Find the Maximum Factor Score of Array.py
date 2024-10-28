class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # Try removing each element
        # Calculate the GCD + LCD of it and return the maximized result


        def lcm(a,b):
            if a < b:
                return lcm(b, a)
            total = a
            while total % b != 0:
                total += a
            return total
        
        def lcm_arr(arr):
            if not arr: return 0
            total = arr[0]
            for num in arr[1:]:
                total = lcm(total, num)
            return total
        
        def gcd(a,b): #gcd(12, 15) -> 3
            while b != 0:
                a,b = b, a % b
            return a
        
        def gcd_arr(arr):
            if not arr: return 0
            total = arr[0]
            for num in arr[1:]:
                total = gcd(total, num)
            return total

        
        res = lcm_arr(nums) * gcd_arr(nums)
        for i in range(len(nums)):
            # Exclude nums[i]
            new_arr = nums[: i] + nums[i+1: ]
            res = max(res, lcm_arr(new_arr) * gcd_arr(new_arr))


        return res
