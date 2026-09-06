class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [n for n in nums if n % 2]
        even = [n for n in nums if n % 2 == 0]
        res = []
        for i in range(len(nums) // 2):
            res.append(even[i])
            res.append(odd[i])
        return res

