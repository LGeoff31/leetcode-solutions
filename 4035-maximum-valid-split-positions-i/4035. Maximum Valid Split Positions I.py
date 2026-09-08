class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        res = 0

        def get_valid_split_positions(arr):
            prefix_gcd = []
            suffix_gcd = []
            curr = 0
            for i in range(len(arr)):
                curr = gcd(curr, arr[i])
                prefix_gcd.append(curr)
            curr = 0
            for i in range(len(arr) -1, -1, -1):
                curr = gcd(curr, arr[i])
                suffix_gcd.append(curr)
            suffix_gcd = suffix_gcd[::-1]
            # print(prefix_gcd, suffix_gcd)
            cnt = 0
            for i in range(len(arr) - 1):
                if prefix_gcd[i] == suffix_gcd[i+1]:
                    cnt += 1
            return cnt

        for i in range(len(nums)):
            new_arr = [nums[j] for j in range(len(nums)) if i != j]
            res = max(res, get_valid_split_positions(new_arr))
        return max(res, get_valid_split_positions(nums))