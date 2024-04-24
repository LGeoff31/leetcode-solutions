class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        far_last = 0
        near_last = 1
        closest_last = 1
        total = 2
        for i in range(n-2):
            tmp1 = closest_last
            tmp2 = near_last
            closest_last = closest_last + near_last + far_last
            near_last = tmp1
            far_last = tmp2
            total = closest_last
        return total

        