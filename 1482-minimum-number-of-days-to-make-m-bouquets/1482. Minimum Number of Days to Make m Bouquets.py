class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: 
            return -1
        
        def calc(day):
            print(day)
            if k == 1:
                bloomDay.sort()
                # print(bloomDay, day, bisect.bisect_right(bloomDay, day))
                return bisect.bisect_right(bloomDay, day)  >= m
            res = 0
            below_day = 0
            l = r = 0
            while r < len(bloomDay):
                if l == r:
                    for i in range(l, l+k):
                        # print(i, bloomDay)
                        if i >= len(bloomDay): break
                        below_day += bloomDay[i] <= day
                    if below_day == k:
                        l = r = l+k
                        below_day = 0
                        res +=1
                    else:
                        r = l+k
                else:
                    if bloomDay[r] <= day:
                        below_day += 1
                    below_day -= bloomDay[l] <= day
                    if below_day == k:
                        below_day = 0
                        l, r = r, r
                        res +=1
                    r+=1
                    l+=1
                # print('res', res, l, r)

            return res >= m

        # Binary Search ???
        res = max(bloomDay)
        l, r = min(bloomDay), max(bloomDay)
        while l <= r: #O(logn)
            mid = l + (r-l) // 2
            # print(mid)
            if calc(mid): #O(n)
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res



        #[x, x, x, x, x]
        