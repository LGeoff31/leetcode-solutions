class Solution:
    def minimumCost(self, n, edges, queries):
        # Initialize the parent array with -1 as initially each node belongs to its own component
        self.parent = [-1] * n
        self.depth = [0] * n

        # All values are initially set to the number with only 1s in its binary representation
        component_cost = [-1] * n

        # Construct the connected components of the graph
        for edge in edges:
            self._union(edge[0], edge[1])

        # Calculate the cost of each component by performing bitwise AND of all edge weights in it
        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]

        answer = []
        for query in queries:
            start, end = query

            # If the two nodes are in different connected components, return -1
            if self._find(start) != self._find(end):
                answer.append(-1)
            else:
                # Find the root of the edge's component
                root = self._find(start)
                # Return the precomputed cost of the component
                answer.append(component_cost[root])

        return answer

    # Find function to return the root (representative) of a node's component
    def _find(self, node):
        # If the node is its own parent, it is the root of the component
        if self.parent[node] == -1:
            return node
        # Otherwise, recursively find the root and apply path compression
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    # Union function to merge the components of two nodes
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        # If the two nodes are already in the same component, do nothing
        if root1 == root2:
            return

        # Union by depth: ensure the root of the deeper tree becomes the parent
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        # Merge the two components by making root1 the parent of root2
        self.parent[root2] = root1

        # If both components had the same depth, increase the depth of the new root
        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1