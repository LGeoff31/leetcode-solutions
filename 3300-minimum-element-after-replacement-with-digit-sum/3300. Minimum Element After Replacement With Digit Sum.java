public class Solution {
    public int minElement(int[] nums) {
        int res = Integer.MAX_VALUE;
        for (int n : nums) {
            int sum = 0;
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            res = Math.min(res, sum);
        }
        return res;
    }
}