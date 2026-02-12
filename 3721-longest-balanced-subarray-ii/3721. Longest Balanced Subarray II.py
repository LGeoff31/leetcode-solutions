class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        mn = [0] * (4 * n)
        mx = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def push(node: int):
            if lazy[node] != 0:
                val = lazy[node]

                for child in (2 * node, 2 * node + 1):
                    mn[child] += val
                    mx[child] += val
                    lazy[child] += val

                lazy[node] = 0

        def update(node: int, segLeft: int, segRight: int, queryLeft: int, queryRight: int, addValue: int):

            if queryLeft > queryRight:
                return
            if queryLeft == segLeft and queryRight == segRight:
                mn[node] += addValue
                mx[node] += addValue
                lazy[node] += addValue
            else:
                push(node)
                mid = (segLeft + segRight) // 2
                update(2 * node, segLeft, mid,
                       queryLeft, min(queryRight, mid), addValue)
                update(2 * node + 1, mid + 1, segRight,
                       max(queryLeft, mid + 1), queryRight, addValue)
                mn[node] = min(mn[2 * node], mn[2 * node + 1])
                mx[node] = max(mx[2 * node], mx[2 * node + 1])
        def findFirst(node: int, segLeft: int, segRight: int, limit: int):
            if segLeft > limit or mn[node] > 0 or mx[node] < 0:
                return -1
            if segLeft == segRight:
                return segLeft
            push(node)
            mid = (segLeft + segRight) // 2
            res = findFirst(2 * node, segLeft, mid, limit)
            if res != -1:
                return res
            if mid < limit:
                return findFirst(2 * node + 1, mid + 1, segRight, limit)
            return -1
        lastPos = [-1] * 100005
        maxLen = 0
        for i in range(n):
            val = nums[i]
            prev = lastPos[val]
            diff = -1 if val % 2 else 1 
            update(1, 0, n - 1, prev + 1, i, diff)
            lastPos[val] = i
            start = findFirst(1, 0, n - 1, i)
            if start != -1:
                maxLen = max(maxLen, i - start + 1)

        return maxLen