class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        up, down, left, right = 0, 0, 0, 0
        res = 0
        for i, c in enumerate(s):
            if c == "N": up += 1
            if c == "S": down += 1
            if c == "W": left += 1
            if c == "E": right += 1

            if right >= left and up >= down:
                ans = right + up
                if k >= left + down:
                    # covers it all
                    ans += left + down
                else:
                    # covers k amount
                    ans = ans + 2*k - (left + down)
                res = max(res, ans)
            if left >= right and up >= down:
                ans = left + up
                if k >= right + down:
                    ans += right + down
                else:
                    ans = ans + 2*k - (right + down)
                res = max(res, ans)
            if right >= left and down >= up:
                ans = right + down
                if k >= left + up:
                    ans += left + up
                else:
                    ans = ans + 2*k - (left + up)
                res = max(res, ans)
            if left >= right and down >= up:
                ans = left + down
                if k >= right + up:
                    ans += right + up
                else:
                    ans = ans + 2*k - (right + up)
                res = max(res, ans)
            # print(res)
        return res
            