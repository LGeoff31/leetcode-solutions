from sortedcontainers import SortedList
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # events.sort()
        events = sorted(events, key = lambda x: x[1])
        # print(events)
        prefix = []
        prefix_values = SortedList()
        res = max([v for s,e,v in events]) # Picking singular event
        for start, end, value in events:
            
            if not prefix:
                prefix_values.add(end)
                prefix.append([start, end, value])
            else:
                # Binary search for the valid index in prefix
        
                idx = bisect_left(prefix_values, start) - 1
                if idx == -1:
                    prefix.append([start, end, max(value, prefix[-1][2])])
                    prefix_values.add(end)
                    continue
                # print('idx', idx, start, end, prefix_values)
                # if len(prefix_values) == idx + 1: idx += 1 
                prefix_value = prefix[idx][2]
                res = max(res, value + prefix_value)
                prefix.append([start, end, max(value, prefix_value, prefix[-1][2])])
                prefix_values.add(end)
            # print(prefix)
        return res
