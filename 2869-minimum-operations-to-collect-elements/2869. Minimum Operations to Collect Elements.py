class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bit = 0
        for i in range(len(nums) -1, -1, -1):
            bit |= (1 << nums[i] - 1)
            print(bit, (1 << (k)) -1) 
            if bit & (1 << (k)) -1 == (1 << (k)) -1:
                return len(nums) - i

        """
        0001 1011

        0011

        """