class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        #1.) find # for all ages[y] <= 100 and ages[y] > (1/2) ages[x] + 7
        #2.) find # for all age[x] >= 100
        res = 0
        print(ages)
        #[20, 30, 100, 110, 120]
        idx_100 = bisect.bisect_right(ages, 100) #3
        for i in range(len(ages)):
            idx_condition_1 = bisect.bisect_right(ages, 0.5*ages[i]+7) #0
            if i < idx_100:
                res += min(i-idx_condition_1, i) if min(i-idx_condition_1, i) > 0 else 0
            else:
                res += i - idx_condition_1 if i - idx_condition_1 > 0 else 0
            print(res)
        a = Counter(ages)
        for key in a:
            if a[key] > 1:
                if key > 0.5*key + 7:
                    res += a[key] * (a[key]-1) // 2
        return res 