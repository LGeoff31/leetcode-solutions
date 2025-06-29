class Solution {
public:
    int minXor(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> p(n+1, 0);
        for (int i = 0; i < n; i++) p[i+1] = p[i] ^ nums[i];
        int max_val = 2 * *max_element(nums.begin(), nums.end()) + 1;
        vector<vector<int>>dp(n+1, vector<int>(k+1, max_val));
        dp[0][0] = 0;
        for (int b = 1; b <= k; b++) {
            for (int a = 1; a <= n; a++) {
                for (int c = b-1; c < a; c++) {
                    dp[a][b] = min(dp[a][b], max(dp[c][b-1], p[a]^p[c]));
                }
            }
        }
        return dp[n][k];
        
    }
};