class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n)) # [0,1,2,3]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a,b):
            parent[find(a)] = find(b) # [3,2,2,3]

        
        # Create the disjoint sets
        for u,v in pairs:
            union(u,v)
            # print(parent)
        index = defaultdict(list)
        characters = defaultdict(list)
        for i in range(len(s)):
            group = find(i) # i belongs to which group
            index[group].append(i)
            characters[group].append(s[i])
        for key in characters:
            characters[key].sort()
        res = [''] * n
        for (i, c) in zip(index.values(), characters.values()):
            for k in range(len(i)):
                res[i[k]] = c[k]

            print(i,c)
        print(index)
        print(characters)

        return "".join(res)
        