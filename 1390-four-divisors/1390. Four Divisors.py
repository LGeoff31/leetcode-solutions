class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def factors(num):
            factors = []
            for i in range(1, ceil(sqrt(num)) + 1):
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
            return list(set(factors))
        res = 0
        for n in nums:
            print(factors(n), n)
            if len(factors(n)) == 4:
                res += sum(factors(n))
        return res 