Link to question: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

## Solution 1

Linear search for the index and return it

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## Solution 2

Attempt binary searching the entire list, check if the array from [left,mid] is sorted, if target is within that range, move right down to mid, otherwise, the target will come afterwards so set left up to mid. If it's not sorted [left.mid], then mid has crossed the barrior of left sorted. If target is within [left,mid], bring down right to mid, otherwise, bring left up to mid. Continue this process so long as left does not exceed right and return the index of target if it is found.

### Analysis

- Time Complexity: `O(logn)`
- Space Complexity: `O(1)`
