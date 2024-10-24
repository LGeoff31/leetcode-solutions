class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        def divisors(num):
            factors = []
            for i in range(1, math.floor(num)+1):
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
            return factors
        
        res = [1e9, -1e9]
        factors = list(set(divisors(area)))
        print(factors)
        for i in range(len(factors)):
            if factors[i] >= area // factors[i] and (factors[i] - area // factors[i]) < res[0] - res[1]:
                res = [factors[i], area // factors[i]]
        return res
