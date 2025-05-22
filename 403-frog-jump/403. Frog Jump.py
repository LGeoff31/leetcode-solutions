class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        @cache
        def dfs(idx, prevJump):
            if idx == len(stones) - 1:
                return True
            if idx >= len(stones):
                return False
            print(idx, prevJump)
            current_position = stones[idx]
            res=False
            if current_position + prevJump - 1 in stones and bisect_left(stones, current_position+prevJump-1) > idx:
                res = res or dfs(bisect_left(stones, current_position+prevJump-1), prevJump-1)
            if current_position + prevJump in stones and bisect_left(stones, current_position+prevJump) > idx:
                res = res or dfs(bisect_left(stones, current_position+prevJump), prevJump)
            if current_position + prevJump + 1 in stones and bisect_left(stones, current_position+prevJump+1) > idx:
                res = res or dfs(bisect_left(stones, current_position+prevJump+1), prevJump+1)
            return res

        return dfs(1, 1)