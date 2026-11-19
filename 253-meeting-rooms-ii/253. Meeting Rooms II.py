class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """
        Problem simplifies to, which vertical line generates the greatest intersection amongst the time intervals
        """

        prefix = [0] * (10 ** 6 + 1)

        for start, end in intervals:
            prefix[start] += 1
            prefix[end] -= 1
        
        prefix = list(accumulate(prefix))
        return max(prefix)