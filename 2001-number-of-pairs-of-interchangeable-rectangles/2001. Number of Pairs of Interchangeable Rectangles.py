class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:    
        cnt = 0
        seen = defaultdict(int)
        for a,b in rectangles:
            seen[b/a] += 1
            cnt += seen[b/a] - 1
        return cnt