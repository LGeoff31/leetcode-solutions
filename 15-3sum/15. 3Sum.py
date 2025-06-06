class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = []
        dic = Counter(nums)
        for key in dic:
            if dic[key] > 3:
                for i in range(3):
                    a.append(key)
            else:
                for i in range(dic[key]):
                    a.append(key)
        nums = a
        res = []
        visited = set()
        for i in range(len(nums)):
            target = -nums[i]
            # Start two sum
            dic = {}
            for j in range(len(nums)):
                if i == j:
                    continue
                
                if nums[j] in dic:
                    a,b,c = nums[i], nums[j], dic[nums[j]]
                    d,e,f = min(a,b,c), a+b+c-min(a,b,c)-max(a,b,c), max(a,b,c)
                    if (d,e,f) not in visited:
                        visited.add((d,e,f))
                        res.append((d,e,f))
                dic[target - nums[j]] = nums[j]
        return res

