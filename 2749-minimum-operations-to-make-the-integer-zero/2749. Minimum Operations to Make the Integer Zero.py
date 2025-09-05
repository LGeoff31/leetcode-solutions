class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def possible(num1, operations):
            subtraction = operations * num2
            target = num1 - subtraction
            steps = 0
            i = 60
            if target == 0 or target < operations: return False
            
            print(target, operations)
            while target > 0:
                if 2 ** i <= target:
                    target -= 2 ** i
                    steps += 1
                i -= 1
            return steps <= operations and target == 0

        for i in range(1, 61):
            if possible(num1, i):
                return i
        return -1