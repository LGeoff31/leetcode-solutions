class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(i, seen):
            if not (0 <= i < len(arr)):
                return False
            if i in seen:
                return False
            seen.add(i)

            if arr[i] == 0:
                return True

            return dfs(i+arr[i], seen) or dfs(i-arr[i], seen)

        # a = {start}
        return dfs(start, set())