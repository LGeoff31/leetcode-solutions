class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #union find algorithm
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

        for i in range(n):
            group = find(i)
            group_i[group].append(i)
            group_ch[group].append(s[i])
        res = [""] * n

        for key in group_i:
            char_arr = group_ch[key]
            char_arr.sort()
            i = 0
            for idx in group_i[key]:
                res[idx] = char_arr[i]
                i+=1
        return "".join(res)
        # print(res)
