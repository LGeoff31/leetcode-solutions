class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        
        res = 1e9
        def calc(arr):
            """ 
            2+3+1


            """
            res = 1e9
            for i in range(len(arr) - 2):
                l,m,r = arr[i], arr[i+1], arr[i+2]
                res = min(res, m-l + r-l + r-m)
            return res

        for key in dic:
            res = min(res, calc(dic[key]))

        return res if res != 1e9 else -1