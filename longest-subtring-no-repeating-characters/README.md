Link to question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Solution 1

This is a brute force approach. Traverse through the string and each iteration will be the beginning of a possible subString of maximum length with no repeating characters. Initialize a global and local counter, and a set. Inside the first loop, loop for the remaining letters following the starting letter and check if is unique by checking if the letter is already in the set. If not, add one to the count and continue until you come across a letter that is not unique aka not in the set. Set the max_count to that count and continue the traversal for all the other letters.

Essentially it generates all possible contiguous substrings to find largest unique substring

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`

## Solution 2

Two Pointers, sliding window algorithm. Utilize set for constant look up. Traverse the right poitner through the string while adding unique values to set, if the right pointer comes across an element that is in the set, update the result counter then remove all element from the left of the set until the duplicate is removed and continue this process.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
