class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Find unqiue tuples * 8
        dic = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dic[nums[i] * nums[j]] += 1
        res = 0
        for key in dic:
            val = dic[key]
            if val >= 2:
                res += val * (val - 1) * 4

        return res