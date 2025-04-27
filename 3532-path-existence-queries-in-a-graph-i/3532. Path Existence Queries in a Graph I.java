class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] color = new int[n];
        int curr = 0;
        // System.out.println(0 + " " + color[0]);
        for(int i = 1; i < n; ++i) {
            if(nums[i] - nums[i - 1] > maxDiff) {
                ++curr;
            }
            color[i] = curr;
            // System.out.println(i + " " + color[i]);
        }

        int m = queries.length;
        boolean[] ans = new boolean[m];
        int i = 0;
        for(int[] query: queries) {
            if(color[query[0]] == color[query[1]]) {
                ans[i++] = true;
            } else {
                ans[i++] = false;
            }
        }

        return ans;
    }
}