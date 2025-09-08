class DSU:
    def __init__(self,n):
        self.parent = {}
        self.size = defaultdict(int)

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent != y_parent:
            if self.size[x_parent] < self.size[y_parent]:
                x_parent, y_parent = y_parent, x_parent
            self.size[x_parent] += self.size[y_parent]
            self.parent[y_parent] = x_parent     

    def find(self, x):
        self.size.setdefault(x, 1)
        self.parent.setdefault(x, x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def group_size(self, x):
        return self.size[x]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """
        Can check for subarray length 1 -> N

        Binary search?!?

        I.e try to find 5 elements with nums[i] >= threshold/5,
        if this isn't possible, would it ever be possible to find 6 elements with nums[i] >= threshold/6, YES potentially
        but would it everb ep ossible to find 4 elemetns with nums[i] >= threshold/4, YES potentially
        So disregard binary search

        """
        union_find = DSU(len(nums))

        sorted_arr = list(reversed(sorted((val, i) for i, val in enumerate(nums))))
        active = [False] * len(nums) # [False, True, True, True, False]
        idx = 0
        # print(sorted_arr)
        for i in range(len(nums)):
            active_threshold = threshold / (i+1) # at each iteration, theshold will DECREASE, so the idx we can binary search will progress
            # Find which indicies have value > threshold
            while idx < len(sorted_arr) and sorted_arr[idx][0] > active_threshold:
                active[sorted_arr[idx][1]] = True
                if sorted_arr[idx][1]-1 >= 0 and active[sorted_arr[idx][1]-1]:
                    union_find.union(sorted_arr[idx][1], sorted_arr[idx][1] - 1) # union(3, 2)
                    # print('unioning', sorted_arr[idx][1], sorted_arr[idx][1] - 1)
                if sorted_arr[idx][1]+1 < len(active) and active[sorted_arr[idx][1]+1]:
                    union_find.union(sorted_arr[idx][1], sorted_arr[idx][1] + 1) # union()
                    # print('unioning', sorted_arr[idx][1], sorted_arr[idx][1] + 1)

                # print(active, union_find.size)
                if union_find.group_size(union_find.find(sorted_arr[idx][1])) >= i+1:
                    return i+1
                idx += 1
        return -1