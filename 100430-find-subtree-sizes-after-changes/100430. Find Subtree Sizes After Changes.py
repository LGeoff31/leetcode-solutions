class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        
        last_seen = {}
        new_parent = parent[:]
    
        def dfs_determine_new_parents(node):
            prev_last_seen = last_seen.get(s[node], None)
            
            if s[node] in last_seen and node != 0:
                new_parent[node] = last_seen[s[node]]
            
            last_seen[s[node]] = node
            
            for child in tree[node]:
                if child != new_parent[node]:  
                    dfs_determine_new_parents(child)
            
            if prev_last_seen is not None:
                last_seen[s[node]] = prev_last_seen
            else:
                del last_seen[s[node]]
        
        tree = defaultdict(list)
        for child in range(1, n):
            tree[parent[child]].append(child)
        
        dfs_determine_new_parents(0)
        
        new_tree = defaultdict(list)
        for child in range(1, n):
            new_tree[new_parent[child]].append(child)
        
        subtree_size = [0] * n
        
        def dfs_subtree_size(node):
            size = 1  
            for child in new_tree[node]:
                size += dfs_subtree_size(child)
            subtree_size[node] = size
            return size
        
        dfs_subtree_size(0)
        
        return subtree_size