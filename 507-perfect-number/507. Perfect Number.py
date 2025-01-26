class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []
        for i in range(1, ceil(num ** 0.5)):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num//i)

        divisors.sort()
        print(divisors)
        return sum(divisors[:-1]) == num