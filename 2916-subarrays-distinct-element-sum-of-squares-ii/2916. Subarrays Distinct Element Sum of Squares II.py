class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, tot = [0] * (n + 1), [0] * (n + 1)  # Fenwick trees over previous-copy positions, stored right to left
        last, ans = {}, 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            c = s = 0
            i = n - p - 1  # boxes 1..n-p-1 hold the positions > p
            while i:
                c += cnt[i]
                s += tot[i]
                i -= i & -i
            ans += (n - r) * ((r - p) ** 2 - 2 * (s - p * c))
            i = n - p  # insert p; p = -1 lands past the end and is skipped
            while i <= n:
                cnt[i] += 1
                tot[i] += p
                i += i & -i
            last[x] = r
        return ans % (10**9 + 7)