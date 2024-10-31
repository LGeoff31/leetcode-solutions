class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @lru_cache(None)
        def dfs(robotIdx, factoryIdx):
            if robotIdx == len(robot):
                return 0
            if factoryIdx == len(factory):
                return float('inf')
            
            res = dfs(robotIdx, factoryIdx + 1)
            cost = 0

            for k in range(factory[factoryIdx][1]):
                if robotIdx + k < len(robot):
                    cost += abs(robot[robotIdx + k] - factory[factoryIdx][0])
                    res = min(res, cost + dfs(robotIdx + k + 1, factoryIdx + 1))

            return res

        return dfs(0, 0)

# Runtime: 937ms Beats 80.00%
# Memory: 24.80MB Beats 47.62%