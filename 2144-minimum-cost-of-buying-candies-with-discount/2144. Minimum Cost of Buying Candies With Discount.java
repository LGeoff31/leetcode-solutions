class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int i = cost.length - 1;
        int bit = 1;
        int res = 0;
        while (i >= 0) {
            if (bit % 3 == 0) {
                i--;
            } else {
                res = res + cost[i];
                i--;
            }
            bit++;
        }
        return res;
    }
}