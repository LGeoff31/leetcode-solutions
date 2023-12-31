Link to question: https://leetcode.com/problems/minimum-window-substring/

## Solution 1

Brute force, basic solution but very slow

### Analysis

- Time Complexity: `O(n^5)`
- Space Complexity: `O(n)`

## Solution 2

Window slider, move the left and right pointers accordingly

- right pointer moves if substring isn't valid under conditions of t
- left pointer moves while the substring is still valid under the conditions of t
- update minimum string each time a new minimum length is found

### Analysis

- Time Complexity: `O(n^3)`
- Space Complexity: `O(n)`

## Solution 3

Window Sliding algorithm

- Create two hashmaps, have a "have" and "need" varaible while traversing the right pointer to gain new substrings
- Once the right pointer has created a valid substring, aka the "have" gained from substring and "need" from t match, then check if the substrings length is less and update the global min_substring index accordingly
- Then increment, left while the substring is still valid, once it is not, decremenet the lost value by 1 and the have value by 1, and continue incrementing right until its once again valid or right has reached the end of the string
- By having the "have" and "need" variables, it allows for O(1) time to check if the current substring is valid against t

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
