from functools import cache
from collections import defaultdict

class Solution:
    # DIDNT DO MYSELF
    def canTraverseAllPairs(self, nums: List[int]) -> bool: 
        if len(nums) == 1:
            return True

        MAXN = 10**5+5
        pf = list(range(MAXN + 1))
        def sieve():
            p = 2
            while p * p <= MAXN:
                if pf[p] == p:
                    for i in range(p * p, MAXN + 1, p):
                        pf[i] = p
                p += 1
            return pf
        pf = sieve()
        @cache
        def fact(n):
            ans = set()
            while n>1:
                f = pf[n]
                ans.add(f)
                while n%f == 0:
                    n //= f
            return ans
        
        factors_list = []
        for x in nums:
            if x == 1:
                return False
            factors_list.append(list(fact(x)))
        graph = defaultdict(set)
        all_factors = set()
        for factors in factors_list:
            for i in range(len(factors)):
                all_factors.add(factors[i])
                for j in range(len(factors)):
                    if i != j:
                        graph[factors[i]].add(factors[j])
                        graph[factors[j]].add(factors[i])
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(next(iter(all_factors)))
        return len(visited) == len(all_factors)