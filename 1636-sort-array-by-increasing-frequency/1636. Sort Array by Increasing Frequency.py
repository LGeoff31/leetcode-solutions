class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        lst = sorted(dic.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for num, freq in lst:
            res.extend([num] * freq)
        return res