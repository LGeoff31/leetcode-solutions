Link to question: https://leetcode.com/problems/longest-consecutive-sequence/description/

## Solution 1

Put all elements in set eliminaiting dups. Look through array, check for starting numbers (aka the number underneath won't be in set), then find the length by doing constant lookups for the next elements if there in the set, and update the max_length

### analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Solution 2

Sort the array, traverse the array and find the length of any consective section in the array (using fact nums[i+1] - nums[i] = 1 for consective), and for each of the sections, make max_length the max_length of all the lengths of the consective secions.

### analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
- **Mutates the linked list**

## Solution 3

Slow and Fast pointers initialized at the head, one goes to next while other goes next twice, if fast node meets slow node, must be cycle

### analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
- **Best Solution**
