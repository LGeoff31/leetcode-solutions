class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res = []
        def score(idx):
            res = 0
            for j in range(idx+1, len(nums)):
                if (nums[i] + nums[j]) % 2:
                    res += 1
            return res

        
        for i in range(len(nums)):
            res.append(score(i))
        return res