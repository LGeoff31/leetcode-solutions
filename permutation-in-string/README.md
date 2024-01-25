Link to question: https://leetcode.com/problems/permutation-in-string/

## Solution 1

Generate every permutation of s1 and check if any of those are in s2. Too slow for AC both memory and time efficiency lol.

### Analysis

- Time Complexity: `O(n! * m)`
- Space Complexity: `O(n!)`

## Solution 2

Another way to tell if a substring can be found as a permutation is by comparing the dequency of each letter and checking it its the same, essentially like an anagram. This reduces the amount operations as you don't have to actually create all the permutations to see if its a permutation.

### Analysis

- Time Complexity: `O(26*n )`
- Space Complexity: `O(1)` max 26 characters

## Solution 2

Have two dictionaries corresponding to s1 and each substring of length s1 in s2. Count the similarities between the two, it its 26 that means all elements are the same so return True aka there permutations. Two pointer sliding window, as you go through if you come across a wanted one increase matches by 1 along with the dictionary, otherwise decremenet it. Note you can replace dictionary with list where ith elements represents the frequency of assci value at that index.

### Analysis

- Time Complexity: `O(n )`
- Space Complexity: `O(1)` max 26 characters
