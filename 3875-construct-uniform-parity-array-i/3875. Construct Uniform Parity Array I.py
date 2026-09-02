class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        nums2_odd = []
        nums2_even = []

        # ODD
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums2_odd.append(nums[i])
            else:
                for j in range(len(nums)):
                    if j!=i and (nums[i]-nums[j])%2==1:
                        nums2_odd.append(nums[i])
                        break

        # EVEN
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums2_even.append(nums[i])
            else:
                for j in range(len(nums)):
                    if j!=i and (nums[i]-nums[j])%2==0:
                        nums2_even.append(nums[i])
                        break
        return len(nums2_odd) == len(nums) or len(nums2_even) == len(nums)