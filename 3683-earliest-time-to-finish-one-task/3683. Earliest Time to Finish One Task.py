class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(x+y for x,y in tasks)