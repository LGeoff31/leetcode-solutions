class Solution:
    def magicalString(self, n: int) -> int:
        lst = [1,2,2]
        idx = 2
        while len(lst) < n + 2:
            val = lst[-1]
            a = lst[idx]
            for i in range(a):
                lst.append(val ^ 3)
            # print(lst, i)
            idx += 1
            # print("i", i)
        # print(lst)
        return lst[:n].count(1)
        # "1221121221221121122……"