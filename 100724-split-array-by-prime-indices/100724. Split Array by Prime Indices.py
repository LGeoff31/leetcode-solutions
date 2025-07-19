class Solution:
    def splitArray(self, nums: List[int]) -> int:
        a,b = [], []

        def isPrime(num):
            if num == 0 or num == 1: return False
            if num == 2: return True
            for i in range(2, ceil(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        for i in range(len(nums)):
            if isPrime(i):
                a.append(nums[i])
            else:
                b.append(nums[i])

        return abs(sum(a) - sum(b))