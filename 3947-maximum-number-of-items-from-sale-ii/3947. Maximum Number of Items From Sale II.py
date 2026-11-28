class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        fact = [0] * (n+1)

        for f, p in items:
            fact[f] += 1
        
        mult = [0] * (n+1)
        for f in range(1, n+1):
            for m in range(f, n + 1, f):
                mult[f] += fact[m]
        
        res = 0
        slots = sorted([(p, mult[f] - 1) for f, p in items])
        pmin = min(p for _, p in items)
        for p, d in slots:
            if d == 0:
                continue
            if p >= 2 * pmin:
                break
            
            k = min(d, budget // p)
            res += 2 * k 
            budget -= k * p
            if k < d:
                break
        res += budget // pmin
        return res