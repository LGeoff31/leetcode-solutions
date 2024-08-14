class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        # The total number of pairs of a array of length n = n(n-1)//2
        # If we pick the middle element and look at the first half of the array, the largest distance is the ends
        # We can calcualte how many pairs that is, if we get 10 pairs but k is 3, we move our right pointer down vice versa
        # Until lets say (i, i+1) -> (6, 10), and we want find k=8, 
        # [1,2,3,4,5,6], k = 8, output: 3
    
        def countPairs(arr, mid):
            res = 0
            l = 0
            for r in range(len(arr)):
                while arr[r] - arr[l] > mid:
                    l += 1
                res += r-l
            return res
        l,r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l+r) // 2
            count = countPairs(nums, mid)
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l