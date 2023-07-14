Link to question: https://leetcode.com/problems/squares-of-a-sorted-array/description/

## Solution 1

Create a list, append all squared numbers into list, return the list sorted

### Analysis

- Time Complexity: `O(nlogn)`
- Space Complexity: `O(n)`

## Solution 2

Left and right pointer on endpoints, check which absolute value is larger, add to end of array, extract only added data and store into result, return result array flipped since the largest values were added first

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
