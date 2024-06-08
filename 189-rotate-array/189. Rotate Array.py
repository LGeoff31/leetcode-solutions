class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,3,4,5,6,7,8], k=26 -> 2
        #[8,7,6,5,4,3,2,1]
        #[6,7,8,1,2,3,4,5]
        k %= len(nums)
        def reverse(start, end):
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        reverse(0, len(nums) - 1) #reverse entire array
        reverse(0, k-1)
        reverse(k, len(nums) - 1)


        







        


        
        