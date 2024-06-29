class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []           #  [1,2,5,6]
        
        for num in nums:
            i = bisect_left(arr,num)          #  How many numbers are after num that are larger
            ans.append(i)                     #  indicie where that number should belong in a sorted list
            del arr[i]                        #  Delete that index
            
        return ans    