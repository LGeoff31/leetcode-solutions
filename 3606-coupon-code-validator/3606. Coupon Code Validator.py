class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        def valid(cd, idx):
            return cd and all(c.isalnum() or c == "_" for c in cd) and isActive[idx] and businessLine[idx] in ["electronics", "grocery", "pharmacy", "restaurant"]

        for i, c in enumerate(code):
            if valid(c, i):
                res.append((businessLine[i], c))
        
        res.sort(key=lambda x: (order[x[0]], x[1]))
        return [c for _, c in res]