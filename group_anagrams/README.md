Link to question: https://leetcode.com/problems/group-anagrams/description/

## Solution 1

Loops through all the nodes, checks if current node is visited, otherwise sets that node to visited, return true is node reached is already visited, else return false once reach end of linked list

### analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`

## Solution 2

Same solution 1, except setting node to None rather than setting it to visited in array

### analysis

- Time Complexity: `O(n^3)`
- Space Complexity: `O(n)`
- **Mutates the linked list**

## Solution 3

Slow and Fast pointers initialized at the head, one goes to next while other goes next twice, if fast node meets slow node, must be cycle

### analysis

- Time Complexity: `O(n * m)`
- Space Complexity: `O(n)`

Where n is the number of elements in strs and m is the average length of all the words in srts

- **Best Solution**
