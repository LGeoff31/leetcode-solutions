class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        lst = [0] * 32
        mask=1


        for i in range(32):
            count = 0
            for num in nums:
                if num & mask:
                    count+=1
            if count >=k:
                lst[i] = 1
            mask <<= 1
        res = 0
        for i in range(len(lst)):
            if lst[i]==1: res += 2**i

        return res


        