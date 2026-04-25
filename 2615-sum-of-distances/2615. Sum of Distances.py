class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        [0, 1, 2, 3]
        [0, 1, 3, 6]

        """
        # [2, 4, 6] -> 4
        dic = defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)
        prefix = {}
        for key in dic:
            prefix[key] = list(accumulate(dic[key]))

        res = []
        for i in range(len(nums)):
            val = nums[i]
            indicies = dic[nums[i]]

            left = bisect_left(indicies, i) # [ 1, 4, 5 ]
            right = len(indicies) - left - 1
            p = prefix[nums[i]]
            left_sum = p[left-1] if left-1 >= 0 else 0
            right_sum = p[-1] - p[left]

            res.append(i*left - left_sum + right_sum - right*i) 

        return res
