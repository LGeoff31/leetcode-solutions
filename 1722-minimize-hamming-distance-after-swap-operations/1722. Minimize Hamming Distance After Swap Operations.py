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
        parent = [i for i in range(n)]
        for e in allowedSwaps:
            union(e[0], e[1])

        d = defaultdict(dict)
        for i in range(n):
            p = find(i)
            if source[i] in d[p]:
                d[p][source[i]] += 1
            else:
                d[p][source[i]] = 1

        ans = 0
        for i in range(n):
            p = find(i)
            if target[i] in d[p] and d[p][target[i]] > 0:
                d[p][target[i]] -= 1
            else:
                ans += 1

        return ans


        