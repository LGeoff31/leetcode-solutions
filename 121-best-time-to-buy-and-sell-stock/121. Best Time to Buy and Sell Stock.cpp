class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int globalMax = 0, l = 0, r = 1;
        while (r < prices.size()) {
            while (r < prices.size() && (prices[r] - prices[l]) > 0) {
                globalMax = max(globalMax, prices[r] - prices[l]);
                r++;
            }
            l = r;
            r++;
        }
        return globalMax;

    }
};