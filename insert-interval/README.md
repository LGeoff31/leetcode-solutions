Link to question: https://leetcode.com/problems/insert-interval/description/

## Solution 1

Check for intersections by traversing through each time slot and checking if neither occurs:

- The new intervals start is after the time slots end (Add the time slot since no intersections up till there)
- The new intervals end is before the time slots start (guaranteed no intersections after this, therefore return res + remainder)

Otherwise there will be an intersection so set newInterval to be the minimum of both start times and the maximum of both end times

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
