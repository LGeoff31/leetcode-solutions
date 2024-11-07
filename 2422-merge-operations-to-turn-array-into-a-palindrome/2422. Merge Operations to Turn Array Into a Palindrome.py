class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = len(nums) - 1
        operations = 0

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[r] != nums[l]:
                if nums[r] < nums[l]:
                    curr = nums[r]
                    while l < r and nums[l] > curr: # Assuming nums[r] < nums[l]
                        r -= 1
                        curr += nums[r]
                        operations += 1

                    nums[r] = curr
                    print(l, r, nums[l], nums[r])

                    if l >= r: return operations
                else:
                    curr = nums[l]
                    while l < r and nums[r] > curr:
                        l += 1
                        curr += nums[l]
                        operations += 1
                    nums[l] = curr
                    print(l, r, nums[l], nums[r], operations)

                    if l >= r: return operations

            l += 1
            r -= 1
            # operations += 1
        print('reached')
        return operations