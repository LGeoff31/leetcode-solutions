class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # Create a graph and run a dfs for each node maintaining a visited set
        dic = {}
        for i in range(len(nums)):
            dic[i] = (i+nums[i])%len(nums)
        # visited = set()
        def dfs(node, visited, method): # method = 1 ? positive : negative
            # print('reached', node, method)
            if nums[node] > 0 and method == False or nums[node] < 0 and method == True:
                return False
            if node in visited:
                return True
            visited.add(node)

            if node != dic[node]:
                return dfs(dic[node], visited, method)
            return False
        for i in range(len(nums)):
            if dfs(i, set(), nums[i] > 0):
                return True
            # print(i, 'reached')
            # print('reached', visited)
        return False