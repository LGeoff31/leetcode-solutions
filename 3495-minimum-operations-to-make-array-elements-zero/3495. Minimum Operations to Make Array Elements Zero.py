class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        lst = [4**i for i in range(100)]
        # print(lst)
        def calc(l, r):
            total = 0
            for i in range(1, len(lst)):
                if lst[i-1] <= l <= lst[i]: # 16 (i=1) <= 16 <= 64
                    if r < lst[i]:
                        total += (r-l+1) * (ceil(log(lst[i], 4)))
                        break
                    else:
                        total += (lst[i] - l) * (ceil(log(lst[i], 4)))
                        l = lst[i]
                # print('total', total)
            return ceil(total / 2)

            
        for l, r in queries:
            res += calc(l, r)
            # print('res', res)
        return res