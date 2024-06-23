class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a,b):
            parent[find(a)] = find(b)
        
        for a,b in pairs:
            union(a,b)
        print(parent)
        group_i = defaultdict(list)
        group_ch = defaultdict(list)

        for i in range(len(s)):
            group = find(i)
            group_i[group].append(i)
            group_ch[group].append(s[i])
        for key in group_ch:
            group_ch[key].sort()
        # a = ["@"] * len(s)
        print(group_i)
        print(group_ch)

        res = ["2"] * n
        for key in group_i:
            indicies = group_i[key]
            for idx, val in enumerate(indicies):
                res[val] = group_ch[key][idx]
    
        return "".join(res)

