Link to question: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs

## Solution 1

- Hash map storing everything where key = a, value=[b,c], where b and c are adjacent to a
- res = [], loop hashmap to find beginning element, whose len(value) = 1, add the beginning to elements to res,
- look last element of res and add the other adj pair and continue until reach endpoint1

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
