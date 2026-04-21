class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            parent[find(a)] = find(b)
        
        n = len(source)
        parent = list(range(len(source)))
        for e in allowedSwaps:
            union(e[0], e[1])

        d = defaultdict(dict)
        for i in range(n):
            p = find(i)
            d[p][source[i]] = 1 + d[p].get(source[i], 0)
        print(d)

        ans = 0
        for i in range(n):
            p = find(i)
            if target[i] in d[p] and d[p][target[i]] > 0:
                d[p][target[i]] -= 1
            else:
                ans += 1

        return ans


        