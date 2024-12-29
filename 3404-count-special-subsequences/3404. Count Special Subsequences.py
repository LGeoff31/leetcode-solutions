class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for p in range(len(nums)):
            for q in range(p+2, len(nums)):
                dic[nums[p] / nums[q]].append(q)
        for key in dic:
            dic[key] = sorted(dic[key])
        res = 0
        # print(dic)
        for r in range(4, len(nums)):
            for s in range(r+2, len(nums)):
                if nums[s] / nums[r] in dic:
                    indicies = dic[nums[s] / nums[r]]
                    # Ensure that 
                    res += bisect_right(indicies, r-2)

        return res