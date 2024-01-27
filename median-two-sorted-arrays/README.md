https://leetcode.com/problems/median-of-two-sorted-arrays/

## Solution 1

It's to slow to merge the two and compute the median. Instead, create a left and right partition for both arrays. If there both valid aka the last element on left partition for array A is less than right element on right partition of B and vice versa, you can simply calculate the median with that information taking in accoutn even and odd cases. Otherwise, binary search to update pointers to either shrink or increase the left partition on both to make it valid.

### Analysis

- Time Complexity: `O(log(m+n))`
- Space Complexity: `O(1)`
