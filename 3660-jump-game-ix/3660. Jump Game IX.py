class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 != root2:
            # if root1 > root2:
            self.parent[root2] = root1

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        start = 0
        curr_max = 0
        uf = UnionFind()
        suffix = [1e9] * (len(nums)+1)

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = min(nums[i], suffix[i+1])

        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            if curr_max <= suffix[i+1]:
                for j in range(start + 1, i+1):
                    uf.union(start, j)

                start = i+1
                if start < len(nums):
                    curr_max = nums[start]
        
        res = [-1] * len(nums)
        comp_max = {}
        for i in range(len(nums)):
            root = uf.find(i)
            comp_max[root] = max(comp_max.get(root, nums[i]), nums[i])

        for i in range(len(nums)):
            res[i] = comp_max[uf.find(i)]
        return res
