class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        """
        1 0 0 8 6

        2 + 3 + 3 + 5 + 3 = 16

        binary search (?)

        """
        nums.sort()
        l, r = 0, len(nums) - 1

        def calc(val):
            return sum(abs(val - n) for n in nums)

        while l <= r:
            m = (l + r) // 2

            mid = nums[m]

            left, middle, right = calc(mid - 1), calc(mid), calc(mid + 1)
            print(left, middle, right)
            if middle < max(left, right):
                return middle
            elif left < right:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1