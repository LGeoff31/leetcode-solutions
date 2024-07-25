class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            leftArr = self.sortArray(nums[0:mid])
            rightArr = self.sortArray(nums[mid:])
            l = r = k = 0
            while l < len(leftArr) and r < len(rightArr):
                if leftArr[l] < rightArr[r]:
                    nums[k] = leftArr[l]
                    l += 1
                else:
                    nums[k] = rightArr[r]
                    r += 1
                k += 1
            
            while l < len(leftArr):
                nums[k] = leftArr[l]
                l+=1
                k+=1
            while r < len(rightArr):
                nums[k] = rightArr[r]
                r+=1
                k+=1
            return nums
        return nums

        