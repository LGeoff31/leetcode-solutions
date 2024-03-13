class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = n*(n+1)//2
        acc = 0

        for i in range(1, n+1):
            acc += i
            if acc == totalSum - acc + i:
                return i
        return -1


        
        