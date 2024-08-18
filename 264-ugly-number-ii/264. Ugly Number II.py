class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a = set()
        a.add(1)
        smallest_num = 1

        for i in range(n):
            smallest_num = min(a)
            a.add(smallest_num * 2)
            a.add(smallest_num * 3)
            a.add(smallest_num * 5)
            a.remove(smallest_num)
        return smallest_num

