class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        for num in nums:
            if num >= k: return 1
        currBit = 0
        bitArr = [0] * 32
        l,r = 0, 0

        def indexes_of_bit_1(bit):
            indexes = []
            for index in range(32):  # assuming 32-bit integer
                if bit & (1 << index):
                    indexes.append(index)
            return indexes
        def get_num_from_arr(arr):
            res = 0
            for i in range(len(arr)):
                if arr[i]:
                    res += 2**i
            return res
        res = 1e9
        while r < len(nums):
            currBit |= nums[r]
            for idx in indexes_of_bit_1(nums[r]):
                bitArr[idx] +=1
            if currBit >= k:
                res = min(res, r-l+1)
                while l < len(nums) and get_num_from_arr(bitArr) >= k:
                    print(nums[l], indexes_of_bit_1(nums[l]))
                    for idx in indexes_of_bit_1(nums[l]):
                        bitArr[idx]-=1
                    l+=1
                    if get_num_from_arr(bitArr) >= k: res = min(res, r-l+1)

            r+=1
        if res == 1e9: return -1
        return res


