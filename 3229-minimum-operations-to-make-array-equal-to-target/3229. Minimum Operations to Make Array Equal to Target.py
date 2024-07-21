class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        res = 0
        prev = 0
        def same_sign(a,b):
            return a * b > 0

        diff = [a-b for a,b in zip(target, nums)]

        for d in diff:
            if same_sign(d, prev):
                if abs(prev) > abs(d):
                    res += abs(prev)  - abs(d) 
            else:
                res += abs(prev)
            prev = d
        return res + abs(prev)
