class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        a = list(map(int, s))
        b = [len(list(group)) for key, group in groupby(a)]

        def check(k):
            if k == 1:
                # 010101
                count = 0
                if a[0] == 0:
                    one = True
                    for i in range(1, len(a)):
                        if one: count += 1 if a[i] == 0 else 0
                        else: count += 1 if a[i] == 1 else 0
                        one = not one
                else:
                    one = False
                    for i in range(1, len(a)):
                        if one: count += 1 if a[i] == 0 else 0
                        else: count += 1 if a[i] == 1 else 0
                        one = not one
                return min(count, len(a) - count)
            return sum(val // (k+1) for val in b)
                        
        l, r = 1, 100000
        while l < r:
            mid = (l+r) // 2
            print('trying', mid, check(mid))
            if check(mid) <= numOps:
                r = mid
            else:
                l = mid + 1
            
        return l