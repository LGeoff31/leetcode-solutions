Link to question: https://leetcode.com/problems/trapping-rain-water/

## Solution 1

Key thing to note is that the problem is very difficult if you think about a two pointer technique or sliding window since you will run into many edge cases where the output can be a lot greater if you use two pointers. Instead come up with a generalized formula for calculating the amount of water that is able to be stored at any ith position. To do this, you must create two monotonic stacks which are stacks which have a strictly increasing or decreasing set of elements.

- Have a stack where the ith index represents the highest height on the left of ith element and do the same for a stack for max height at right
- Formula of height at ith index = min(maxLeft,maxRight) - height[i]

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
