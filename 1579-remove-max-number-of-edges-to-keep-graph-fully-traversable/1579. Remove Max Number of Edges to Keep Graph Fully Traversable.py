class UnionFind():
    def __init__(self, n):
        self.count = n # Number of disjoint sets
        self.parent = list(range(n))
        self.rank = [1] * n # Size of subtree
    
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False # Connected graph
        self.count -= 1 # One more connection, one less disjoint
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # Add small sub-tree to large sub-tree
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True # Union was made

        self.parent[find(p)] = self.parent[find(q)]
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Group nodes into connected components, then remove edges that are not necessary
        # Sort edges from type 3 -> 2 -> 1
        # Create union find data structure, one for Alice, one for Bob
        # Iterate through edges
            # Type 3: Try unite nodes in both Alice + Bob's DSU, if union successful, increment edgeAdd counter
            # Type 2: Try unite node Bob's DSU, and do same
            # Type 1: Try unite node Alice's DSU, and do same
        # After processing all edges, check Alice and Bob have single connected component (DSU's are connected)
            # If so, return number edges that were not added (edges.length - edgeAdd)
            # Otherwise, return -1
        ans = 0
        edges.sort(reverse=True)
        ufa = UnionFind(n)
        ufb = UnionFind(n)
        for t, u, v in edges:
            u, v = u-1, v-1
            if t == 1:
                ans += not(ufa.union(u,v))
            elif t == 2:
                ans += not(ufb.union(u,v))
            else:
                ans += not(ufa.union(u, v) and ufb.union(u,v))
        return ans if ufa.count == 1 and ufb.count == 1 else - 1