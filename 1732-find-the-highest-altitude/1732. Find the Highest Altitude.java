class Solution {
    public int largestAltitude(int[] gain) {
        int maxHeight = 0;
        int n = 0;
        for (int g : gain) {
            n += g;
            maxHeight = Math.max(maxHeight, n);
        }
        return maxHeight;

    }
}