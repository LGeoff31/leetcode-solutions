class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        dic = {} # price: beauty
        for price, beauty in items:
            if price in dic:
                dic[price] = max(dic[price], beauty)
            else:
                dic[price] = beauty
        lst = []
        for key in dic:
            lst.append([key, dic[key]])
        lst.sort()
        prefix=[lst[0][1]]
        for i in range(1, len(lst)):
            prefix.append(max(prefix[-1], lst[i][1]))
        # print(prefix)
        res = []
        a = [x for x,y in lst]
        # print('a', a)
        for i in range(len(queries)):
            # [1,2,3,4,5,6]
            idx = bisect_left(a, queries[i])
            if idx >= len(a):
                res.append(prefix[-1])
                continue
            if a[idx] == queries[i]:
                res.append(prefix[idx])
            elif a[idx - 1] < queries[i]:
                res.append(prefix[idx - 1])
            else:
                res.append(0)
            # print("res", res)
            
        return res