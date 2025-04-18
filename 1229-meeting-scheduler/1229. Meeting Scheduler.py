class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i,j = 0, 0
        while i < len(slots1) and j < len(slots2):
            # Check if there is an intersection
            dur = 0
            if slots2[j][0] <= slots1[i][1] and slots2[j][0] >= slots1[i][0]:
                dur = min(slots1[i][1], slots2[j][1]) - slots2[j][0]
            elif slots2[j][1] >= slots1[i][0] and slots2[j][1] <= slots1[i][1]:
                dur = slots2[j][1] - max(slots2[j][0], slots1[i][0])
            elif slots2[j][0] <= slots1[i][0] and slots2[j][1] >= slots1[i][1]:
                dur = slots1[i][1] - slots1[i][0]
            print(dur)
            if dur >= duration:
                return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
            
            # Which to increment
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []