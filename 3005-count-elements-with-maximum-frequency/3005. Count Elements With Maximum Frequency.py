class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        a = max(dic.values())
        return sum(dic[key] for key in dic if dic[key] == a)