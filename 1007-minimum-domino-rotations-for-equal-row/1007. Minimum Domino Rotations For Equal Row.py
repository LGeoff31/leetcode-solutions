class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        r = 1e9
        for i in range(1, 7):
            a = 0
            valid = True
            for idx,n in enumerate(tops):
                if n != i:
                    if bottoms[idx] != i:
                        valid = False
                    a += 1
            if valid:
                r = min(r, a)
        

        for i in range(1, 7):
            a = 0
            valid = True
            for idx,n in enumerate(bottoms):
                if n != i:
                    if tops[idx] != i:
                        valid = False
                    a += 1
            if valid:
                r = min(r, a)
        return r if r != 1e9 else -1