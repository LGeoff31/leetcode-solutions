class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        def ascend(arr):
            for i in range(1, len(arr)):
                if arr[i] != arr[i-1] + 1:
                    return False
            return True
        for i in range(len(nums) - k + 1):
            subarr = nums[i:i+k]
            print(subarr)
            if ascend(subarr):
                res.append(nums[i+k-1])
            else:
                res.append(-1)
        return res
        