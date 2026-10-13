class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        fibs = [0, 1]

        for _ in range(1000):
            fibs.append(fibs[-1] + fibs[-2])

        for i in range(len(fibs) - 2):
            if fibs[i] + fibs[i+1] + fibs[i+2] == n:
                return True
        return False

