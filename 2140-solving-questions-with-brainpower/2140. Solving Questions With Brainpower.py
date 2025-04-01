class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i >= len(questions):
                return 0
            res = 0

            # TAKE
            res = max(res, questions[i][0] + dfs(i + questions[i][1] + 1))
            # DONT TAKE
            res = max(res, dfs(i+1))

            return res


        return dfs(0)