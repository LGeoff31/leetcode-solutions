class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1 
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        subtree_size = [0] * n
        
        def dfs(node, parent):
            size = 1
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                size += dfs(neighbor, node)
            subtree_size[node] = size
            return size
        
        dfs(0, -1)
        
        good_nodes = 0
        
        def is_good(node):
            child_sizes = []
            for neighbor in adj[node]:
                if subtree_size[neighbor] < subtree_size[node]:
                    child_sizes.append(subtree_size[neighbor])
            
            if len(set(child_sizes)) <= 1: 
                return True
            return False
        
        for node in range(n):
            if is_good(node):
                good_nodes += 1
        return good_nodes