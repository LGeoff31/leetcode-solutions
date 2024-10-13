class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        def eval(nums):
            a = Counter(nums)
            if len(a) <= x:
                return sum(nums)
            b = sorted([(a[key], key) for key in a], reverse=True, key=lambda x: (x[0], x[1]))
            ans = 0
            for i in range(x):
                ans += b[i][1] * b[i][0]
            return ans
        
        for i in range(len(nums) - k + 1):
            ans[i] = eval(nums[i:i+k])

        return ans