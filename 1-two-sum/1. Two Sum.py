class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in dic:
                return [i,dic[compl]]

            dic[nums[i]] = i