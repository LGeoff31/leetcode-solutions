class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for a in operations:
            if "+" in a:
                res += 1
            else:
                res -= 1
        return res