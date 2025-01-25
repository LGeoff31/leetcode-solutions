class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            a.append((nums[i], i))
        a.sort()
        lst = []
        curr = []
        idx = 0
        # Create disjoint sets
        while idx < len(a):
            if not curr:
                curr.append((a[idx][0], a[idx][1]))
                idx += 1
                continue

            if abs(a[idx][0] - curr[-1][0]) <= limit:
                curr.append((a[idx][0], a[idx][1]))
            else:
                lst.append(curr)
                curr = [(a[idx][0], a[idx][1])]
            idx += 1
        if curr:
            lst.append(curr)
        res = [0] * len(nums)
        for arr in lst:
            idx_lst = []
            for val, idx in arr:
                idx_lst.append(idx)
            idx_lst.sort()
            for i in range(len(arr)):
                res[idx_lst[i]] = arr[i][0]

        print(lst)

        return res