Link to question: https://leetcode.com/problems/container-with-most-water/

## Solution 1

- Perform a nested loop generating every pair and calcualte the volume, and update the max_volume counter accordingly.

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`

## Solution 2

- Have left and right pointers
- Loop should terminate when left and right overlap
- Calculate the water at each of these processes as you increment/decremenet the right and left pointers
- Find the minimum height between left and right pointers, if left has lower height, incremenent left pointer and vice versa

### Analysis 2

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
