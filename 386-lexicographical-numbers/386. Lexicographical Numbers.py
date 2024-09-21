class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n+1)]
        # Digit can have at most 5 digits
        # res = sorted(res, key = lambda : x: )
        res.sort()
        for i in range(len(res)):
            res[i] = int(res[i])
        return res