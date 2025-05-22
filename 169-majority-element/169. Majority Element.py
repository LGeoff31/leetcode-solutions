class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        a,b = 0, 0
        for key in dic:
            if dic[key] > len(nums) // 2:
                a = key
        return a