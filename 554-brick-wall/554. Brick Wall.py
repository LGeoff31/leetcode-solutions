class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        unique_numbers = set()
        lst = []
        for arr in wall:
            a = set()
            curr = 0
            for elem in arr:
                curr += elem
                unique_numbers.add(curr)
                a.add(curr)
            lst.append(a)
        res = 1e9
        print(lst)
        for num in unique_numbers:
            if num == 0 or num == sum(wall[0]): continue
            c = 0
            for arr_set in lst:
                if num in arr_set:
                    c += 1
            res = min(res, len(wall)-c)
            print(res, num)
        return min(res, len(wall))