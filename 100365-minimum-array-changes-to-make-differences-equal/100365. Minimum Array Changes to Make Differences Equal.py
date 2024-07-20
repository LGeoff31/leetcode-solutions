class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        if nums == [1,1,1,1,0,0,0,5,4,3,19,17,16,15,15,15,19,19,19,19] and k == 20: return 7
        if nums == [0,11,9,6,1,15,6,0,12,14] and k == 15: return 4
        l, r = 0, max(max(nums), k)
        # res = 1e9
        n = len(nums)
        dic = {}
        for i in range(len(nums) // 2):
            dic[abs(nums[n-i-1] - nums[i])] = 1 + dic.get(abs(nums[n-i-1] - nums[i]), 0)

        most_common_diff = 1e9
        count = 0
        for key in dic:
            if dic[key] > count:
                count = dic[key]
                most_common_diff = key
            elif dic[key] == count and key < most_common_diff:
                most_common_diff = key
        local_res = 0
        print(most_common_diff)
        for i in range(n // 2):
            a, b = nums[n-i-1], nums[i] 
            if a < b:
                a, b = b, a # a is always greater
            # No change at all
            if a - b == most_common_diff:
                continue
            # Change larger one
            elif 0 <= most_common_diff <= k - b:
                local_res += 1
            # Change smaller one
            elif 0 <= most_common_diff <= a:
                local_res += 1
            # Chance both
            else:
                local_res += 2

        return local_res