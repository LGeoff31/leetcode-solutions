class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i,j = 0, 0

        def intersect(s,e):
            s1,e1 = s
            s2,e2 = e
            return (-1, -1) if e1 < s2 or s1 > e2 else (max(s1, s2), min(e1, e2))
        while i < len(slots1) and j < len(slots2):
            s,e = intersect(slots1[i], slots2[j])
            if s != -1 and e != -1:
                if e-s >= duration:
                    return [s, s+duration]
            
            # Which to increment
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []