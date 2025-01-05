class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        lst = []
        for i in range(32):
            count = 0
            mask = 1 << i
            print(nums[0], mask, nums[0] ^ mask)
            for num in nums:
                if num & mask:
                    count += 1
            lst.append(count)
        print(lst)
        n = len(nums)
        res = 0
        for numberBits in lst:
            # If there are 3 numbers with bit 1 and 5 numbers without
            res += numberBits * (n - numberBits)
        return res