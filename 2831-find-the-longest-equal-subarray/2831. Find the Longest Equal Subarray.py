class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)

        res = 0

        for indices in dic.values():
            l = 0
            for r in range(len(indices)):
                # Number of elements to remove = total range size - number of matching values
                while indices[r] - indices[l] - (r - l) > k:
                    l += 1
                res = max(res, r - l + 1)
        
        return res