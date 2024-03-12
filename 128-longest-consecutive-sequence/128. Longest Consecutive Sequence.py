class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums_map = {}
        longest_consecutive = 0
        for num in nums:
            if num not in nums_map:
                nums_map[num] = [num, num]
                left = num
                right = num

                # left neighbor - extend left range
                if num - 1 in nums_map:
                    left = nums_map[num - 1][0]

                # right neighbor - extend right range
                if num + 1 in nums_map:
                    right = nums_map[num + 1][1]

                nums_map[left] = [left, right]
                nums_map[right] = [left, right]
                longest_consecutive = max(longest_consecutive, right - left + 1)

        return longest_consecutive


            
