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
        
        group_i = defaultdict(list)
        group_ch = defaultdict(list)

        for i in range(len(s)):
            group = find(i)
            group_i[group].append(i)
            group_ch[group].append(s[i])
        for key in group_ch:
            group_ch[key] = sorted(group_ch[key], reverse=True)
        a = ["@"] * len(s)
        res = ""
        for i in parent:
            res += group_ch[i][-1]
            group_ch[i].pop()
        return res



        print(group_i)
        print(group_ch)

