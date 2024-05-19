class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        bad = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                bad.append(i)
        print(bad)
        res = []
        for start, end in queries:
            idx_left = bisect.bisect_left(bad, start)
            idx_right = bisect.bisect_left(bad, end)
            print("idx", idx_left, idx_right)

            if idx_left != idx_right:
                res.append(False)
            else:
                res.append(True)

        return res