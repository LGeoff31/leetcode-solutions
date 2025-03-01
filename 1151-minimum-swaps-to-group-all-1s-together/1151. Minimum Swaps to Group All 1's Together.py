class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)
        zeros = 0
        for i in range(ones):
            if data[i] == 0:
                zeros += 1
        res = zeros
        l = 0
        for i in range(ones, len(data)):
            if data[i] == 0:
                zeros += 1
            if data[l] == 0:
                zeros -= 1
            l += 1
            res = min(res, zeros)
        return res