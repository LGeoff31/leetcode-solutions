import bisect


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        # run binary search on smaller
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # case odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                # case even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
