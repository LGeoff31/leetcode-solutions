class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def change(arr):
            for i in range(len(arr)):
                arr[i] = mapping[arr[i]]
            return sum( [arr[i] * 10 ** (len(arr) - i - 1) for i in range(len(arr)) ] )
        
        lst = []
        for i in range(len(nums)):
            lst.append([change([int(num) for num in str(nums[i]) ]), i, nums[i]])
        lst.sort()
        return [c for a,b,c in lst]

        
        