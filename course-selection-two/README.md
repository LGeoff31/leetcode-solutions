Link to question: https://leetcode.com/problems/course-schedule-ii/

## Solution 1

Create a hashmap where
key = course
value = list of preq's

Loop through each course and run a dfs on it. In the dfs, it should continue dfs'ing through the preq list until you come to a empty one which then you can add to output, mark as visited and as your dfs backtrack, it will continue adding to output in the correct order. Note that it is possible that it will never come to a course with empty preq's and this is the case of a cycle. Simply have a cycle set that lets you know the current courses you've visited during that dfs duration so you can simply retunr [] if there is a cycle.

### Analysis

-loop through each node and for each node, look at at mode all the edges

- Time Complexity: `O(n+m)`
- Space Complexity: `O(n)`
