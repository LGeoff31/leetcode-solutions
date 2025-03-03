class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        dic = {}

        for i in range(len(nums)):
            # if nums[i] == i: continue
            dic[nums[i]] = nums[nums[i]]
        print(dic)
        def explore(num):
            if num not in visited:
                visited.add(num)
                return 1 + explore(nums[num])
            return 0
        res = 0
        for num in nums:
            if num not in visited:
                # visited.add(num)
                res = max(res, explore(num))
        return res