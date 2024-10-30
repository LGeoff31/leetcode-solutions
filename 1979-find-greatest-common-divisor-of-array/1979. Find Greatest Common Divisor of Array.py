class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b): # 15, 12 -> 12, 3 -> 3, 0
            if a < b:
                return gcd(b,a)
            while b != 0:
                a, b = b, a % b
            return a
        return gcd(min(nums), max(nums))