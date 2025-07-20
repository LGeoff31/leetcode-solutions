class SegmentTree:
    def __init__(self, data, max_depth=6):
        self.n = len(data) # [1,2,3,4]
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [Counter() for _ in range(2 * self.size)]

        for i in range(self.n):
            d = SegmentTree.depth(data[i])
            self.tree[self.size + i][d] += 1 # increase depth counter by 1 for leaf node
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1] # left node + right node range queried
            
    @staticmethod
    def depth(x, memo={}):
        if x in memo:
            return memo[x]
        org = x
        steps = 0
        while x > 1:
            x = bin(x).count('1')
            steps += 1
        memo[org] = steps
        return steps
    def update(self, index, value):
        idx = self.size + index
        self.tree[idx] = Counter()
        self.tree[idx][SegmentTree.depth(value)] += 1
        idx //= 2
        while idx > 0:
            self.tree[idx] = self.tree[2*idx] + self.tree[2*idx+1]
            idx //= 2
    def query(self, l, r, k):
        # print(self.tree)
        l += self.size
        r += self.size # inclusive
        res = 0
        while l <= r:
            if l % 2 == 1:
                # Single node on left
                res += self.tree[l][k]
                l += 1
            if r % 2 == 0:
                # single node on right
                res += self.tree[r][k]
                r -= 1
            l //= 2
            r //= 2
        return res
        

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Segment tree?!
        Note with num <= 10**15, 10*15 -> 15 -> 4 -> 1 -> DONE
        what if we have a counter with all nums and precompute depth each
        then have a segment tree of ranged indicies (i, j) which tell us the number of groups values for each popcount (1-5)
        this way updating a value will be updated in logn time in the segment tree
        O(nlogn)
        """
        tree = SegmentTree(nums)
        res = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                res.append(tree.query(l, r, k))
            else:
                _, idx ,val = q
                tree.update(idx, val)
        return res