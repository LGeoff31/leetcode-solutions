Link to question: https://leetcode.com/problems/h-index/

## Solution 1

Loop through all elements from the minimum to maximum of candidates and check if there are that many elements more than the current index

### analysis

- Time Complexity: `O(n * (max(n)- min(n))`
- Space Complexity: `O(1)`

## Solution 2

Sort the array and check if for the current number in the array if the remainind elemnets aka len(nums) - i is within subset of number.

### analysis

- Time Complexity: `O(nlogn)`
- Space Complexity: `O(1)`
