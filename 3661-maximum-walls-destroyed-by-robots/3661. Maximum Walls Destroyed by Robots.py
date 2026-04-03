class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        """
        2.     10

        """
        walls.sort()
        lst = [(robots[i], distance[i]) for i in range(len(robots))]
        lst.sort()
        @cache
        def dfs(robot_idx, walls_idx):
            if robot_idx == len(robots) or walls_idx == len(walls):
                return 0

            res = 0
            # have robot shoot left
            robot_pos = lst[robot_idx][0]
            robot_dis = lst[robot_idx][1]
            right_bound = bisect_right(walls, robot_pos)
            left_bound = bisect_left(walls, robot_pos - robot_dis)
            if robot_idx > 0 and lst[robot_idx - 1][0] >= robot_pos - robot_dis:
                left_bound = bisect_right(walls, lst[robot_idx - 1][0])
            start = max(left_bound, walls_idx)
            hit_walls = right_bound - start
            res = max(res, max(hit_walls,0) + dfs(robot_idx + 1, max(walls_idx, right_bound)))
            # have robot shoot right
            nxt_idx = bisect_right(walls, robot_pos + robot_dis)
            if robot_idx + 1 < len(lst) and lst[robot_idx + 1][0] <= robot_pos + robot_dis:
                nxt_idx = bisect_left(walls, lst[robot_idx + 1][0])
            _start = max(walls_idx, bisect_left(walls, robot_pos))
            _hit_walls = nxt_idx - _start
            res = max(res, max(_hit_walls,0) + dfs(robot_idx + 1, nxt_idx))
            return res
        return dfs(0, 0)
