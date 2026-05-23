class Solution {
    public boolean check(int[] nums) {
        int decreases = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[((i+1)+nums.length) % nums.length]) {
                decreases++;
            }
        }
        return decreases<=1;
    }
}