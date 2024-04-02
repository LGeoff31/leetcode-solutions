class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        #generate pairs array [i,j] denoting the indexes i and j can be swapped
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        a = copy.deepcopy(nums)
        a.sort()
        pairs = []
        for i in range(1, len(a)):
            if a[i] - a[i-1] <= limit:
                for elem1 in dic[a[i]]:
                    for elem2 in dic[a[i-1]]:
                        pairs.append([elem1, elem2])



        # print(pairs, nums)
        parent = list(range(len(nums)))
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
    
        def union(a,b):
            parent[find(a)] = find(b)
        for a,b in pairs:
            union(a,b)
        
        group_c = defaultdict(list)

        for i in range(len(nums)):
            group = find(i)
            group_c[group].append(nums[i])
        res = []
        for key in group_c:
            group_c[key] = sorted(group_c[key], reverse=True)
        # print(group_c)
        for i in parent:
            res.append(group_c[i][-1])
            group_c[i].pop()

        return res
        
         