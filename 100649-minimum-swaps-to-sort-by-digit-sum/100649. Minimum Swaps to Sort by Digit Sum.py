class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # (9,18), (7,43), (7,34), (7,16)
        sorted_lst = []
        for i, num in enumerate(nums):
            sorted_lst.append((sum(int(c) for c in str(num)), num, i))
        sorted_lst.sort()
        idx = 0
        res = 0
        temp_arr = nums.copy()
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        # print(sorted_lst)
        while idx < len(nums):
            if nums[idx] != sorted_lst[idx][1]:
                i = dic[sorted_lst[idx][1]] 
                dic[nums[idx]] = i
                dic[nums[i]] = idx
                # print('performing swap', idx, i)
                nums[idx], nums[i] = nums[i], nums[idx]
                res += 1
            idx += 1
            # print(nums)

        return res
        