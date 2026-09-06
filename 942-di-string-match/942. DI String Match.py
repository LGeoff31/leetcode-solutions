class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """

        IIDIDD = 6

        [0, 4, 5, 3, 6, 2, 1]

        [0, 2]

        []
        """
        l, r = 0, len(s)
        res = []
        for c in s:
            if c == "I":
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
                
        res.append(r)        
        return res
