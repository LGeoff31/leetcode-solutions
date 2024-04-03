class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        if zero1==0 and zero2==0:
            if sum(nums1)==sum(nums2): return sum(nums1)
            return -1
        if sum(nums1) == sum(nums2):
            diff = sum(nums1) - sum(nums2)
            if zero2 > diff and zero1 == 0: return -1
            elif zero2:
                return sum(nums1) + max(zero1, zero2)
            return -1
        elif sum(nums1) > sum(nums2):
            diff = sum(nums1) - sum(nums2)
            if zero2 > diff and zero1 == 0: return -1
            elif zero2:
                return max(sum(nums2) + zero2, sum(nums1) + zero1)
            return -1
        else: #[3,2,0,1,0], nums2 = [6,5,0] 
            diff = sum(nums2) - sum(nums1)
            print(sum(nums2), sum(nums1), diff, zero1, zero2)
            if zero1 > diff and zero2 == 0: return -1
            elif zero1:
                return max(sum(nums2) + zero2, sum(nums1) + zero1)
            return -1

        