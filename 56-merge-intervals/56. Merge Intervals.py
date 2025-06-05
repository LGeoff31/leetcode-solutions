class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]

            if stack[-1][-1] < s:
                # No overlap
                stack.append(intervals[i])
            else:
                # Overlap
                org_s, org_e = stack.pop()
                stack.append([org_s, max(org_e, e)])
        
        return stack