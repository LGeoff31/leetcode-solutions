class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()  #store tuples 
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            dic = {}
            for j in range(i+1, len(nums)):
                if target - nums[j] in dic:
                    if (nums[i], nums[j], target-nums[j]) not in visited:
                        res.append([nums[i], nums[j], target - nums[j]])
                        visited.add((nums[i], nums[j], target-nums[j]))
                else:
                    dic[nums[j]] = j
        
        return res