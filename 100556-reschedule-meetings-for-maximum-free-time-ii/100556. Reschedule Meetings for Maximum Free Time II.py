class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        num_meetings = len(startTime)
        free_intervals = [0] * (num_meetings + 1)
    
        free_intervals[0] = startTime[0] - 0
        for i in range(1, num_meetings):
            free_intervals[i] = startTime[i] - endTime[i - 1]
        free_intervals[num_meetings] = eventTime - endTime[num_meetings - 1]
    
        max_initial_free_time = max(free_intervals)
    
        left_max_intervals = [0] * (num_meetings + 1)
        right_max_intervals = [0] * (num_meetings + 1)
    
        left_max_intervals[0] = free_intervals[0]
        for i in range(1, num_meetings + 1):
            left_max_intervals[i] = max(left_max_intervals[i - 1], free_intervals[i])
    
        right_max_intervals[num_meetings] = free_intervals[num_meetings]
        for i in range(num_meetings - 1, -1, -1):
            right_max_intervals[i] = max(right_max_intervals[i + 1], free_intervals[i])
    
        max_free_time = max_initial_free_time
        for i in range(num_meetings):
            meeting_duration = endTime[i] - startTime[i]
    
            if i == 0:
                expanded_gap = free_intervals[0] + meeting_duration + (free_intervals[1] if num_meetings >= 2 else 0)
                max_other_gaps = right_max_intervals[2] if num_meetings > 1 else 0
            elif i == num_meetings - 1:
                expanded_gap = free_intervals[num_meetings - 1] + meeting_duration + free_intervals[num_meetings]
                max_other_gaps = left_max_intervals[num_meetings - 2] if num_meetings > 1 else 0
            else:
                expanded_gap = free_intervals[i] + meeting_duration + free_intervals[i + 1]
                left_max = left_max_intervals[i - 1] if i - 1 >= 0 else 0
                right_max = right_max_intervals[i + 2] if i + 2 < num_meetings + 1 else 0
                max_other_gaps = max(left_max, right_max)
    
            if max_other_gaps >= meeting_duration:
                candidate_free_time = expanded_gap
            else:
                candidate_free_time = expanded_gap - meeting_duration
    
            max_free_time = max(max_free_time, candidate_free_time)
    
        return max_free_time