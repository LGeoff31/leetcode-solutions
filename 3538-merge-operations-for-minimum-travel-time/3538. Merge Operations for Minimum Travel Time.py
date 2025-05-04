class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        @cache
        def dfs(idx, prev_pos, speed, extra_speed, left):
            if idx == n - 1:
                return (position[idx] - prev_pos) * speed if left == 0 else 1e9
            
            if left:
                cost = (position[idx] - prev_pos) * speed
                take = cost + dfs(idx + 1, position[idx], time[idx] + extra_speed, 0, left)
                no_take = dfs(idx+1, prev_pos, speed, extra_speed + time[idx], left - 1)
                return min(take, no_take)
            cost = (position[idx] - prev_pos) * speed
            take = cost + dfs(idx + 1, position[idx], time[idx] + extra_speed, 0, left)
            return take

        return dfs(1, 0, time[0], 0, k)
            