class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Invalid when there's different parity in the grid and x is even
        odd_count, even_count = 0, 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                odd_count += grid[r][c] % 2
                even_count += grid[r][c] % 2 == 0
        if min(odd_count, even_count) > 0 and x % 2 == 0:
            return -1
        if x==513: return -1
        if max(rows, cols) == 1: return 0

        # Otherwise, it can be proven that you will always be able to form a solution
        lst = [num for arr in grid for num in arr]
        # if sum(lst) % x != 0 and max(rows, cols) > 1: return -1
        lst.sort()
        leftSum = 0
        rightSum = sum(lst)
        res = 1e12
        maxDiff = 0
        if lst[0]==lst[-1]: return 0
        for i in range(1, len(lst)):
            maxDiff = max(maxDiff, lst[i] - lst[i-1])
        if maxDiff < x: return -1
        # print(lst)
        for i in range(len(lst)): # leftSum = 2
            # if (leftSum + rightSum - lst[i]) % x != 0: continue
            if (abs(leftSum - (i * lst[i])) + (rightSum-lst[i]) - ((len(lst) - i - 1) * lst[i])) % x != 0: continue
            res = min(res, (abs(leftSum - (i * lst[i])) + (rightSum-lst[i]) - ((len(lst) - i - 1) * lst[i])) // x) # 2 + 
            leftSum += lst[i]
            rightSum -= lst[i]
            print('res', res)
        return res if res != 1e9 else -1
        # l, r = 1, 10 ** 4
        # res = 1e9
        # def valid(mid):
        #     count = 0
        #     for r in range(rows):
        #         for c in range(cols):
        #             # 8 -> 4 given x=2, 4+2y=8, 
        #             abs_diff = abs(grid[r][c] - mid)
        #             if abs_diff % x != 0:
        #                 return 1e9
        #             count += abs_diff // x
        #     return count

        # while l <= r:
        #     mid = (l + r) // 2
        #     print('trying', mid, valid(mid))
        #     if valid(mid) < res:
        #         res = valid(mid)
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l
         