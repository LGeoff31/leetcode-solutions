https://leetcode.com/problems/daily-temperatures/description/

## Solution 1

Problem which can easily be done in n^2 but can be improved by using a stack.

- As you traverse, if you notice that the last elements in the stack is smaller than the one you're currently at, you can simply subtract the two indicies and add it to result

- If the one you're currently one is smaller, continue adding values until it doesn't, this will look like a monotonic decreasing stack

- Make sure that when you pop when your number is bigger than the last, you continue doing this until it no longer holds, make sure add indexes into the stack as well so this can be done

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
