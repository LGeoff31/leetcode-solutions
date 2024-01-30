Link to question: https://leetcode.com/problems/subarray-sum-equals-k/description/

## Solution 1

Create prefix sum array. The idea is loop through indexes, at the ith index, determine the prefix sum up to i, you want a subarray with value of that prefix sum - k. If that value is in the dictionary add the count assciated to how many times that value has occured in the subarrays thus far, if not, build that hashmap by adding that prefix sum value essentially saying up until that point, you can generate a value of that value.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
