class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return 

        if self.size[parent_a] > self.size[parent_b]:
            self.size[parent_a] += self.size[parent_b]
            self.parent[parent_b] = parent_a
        else:
            self.size[parent_b] += self.size[parent_a]
            self.parent[parent_a] = parent_b
    
    def find(self, a):
        self.parent.setdefault(a, a)
        self.size.setdefault(a, 1)

        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        formatted_nums = [(n, i) for i, n in enumerate(nums)]
        formatted_nums.sort()
        union_find = UnionFind()
        union_find.union(0, 0)


        for i in range(1, len(formatted_nums)):
            if formatted_nums[i][0] - formatted_nums[i-1][0] <= limit:
                union_find.union(formatted_nums[i][1], formatted_nums[i-1][1])
            union_find.union(i, i)
        
        sorted_values_by_group = defaultdict(list)
        for idx, parent in union_find.parent.items():
            sorted_values_by_group[parent].append((nums[idx], idx))
        res = [0] * len(nums)
        for parent in sorted_values_by_group:
            values = sorted_values_by_group[parent]
            values.sort()
            indexes = [idx for val, idx in values]
            indexes.sort()
            for i, idx in enumerate(indexes):
                res[idx] = values[i][0]

        return res