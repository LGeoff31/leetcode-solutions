class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int l = 0, r = 1;
        while (r < prices.size() && prices[l] >= prices[r]) {
            l++;
            r++;
        } 

        while (r < prices.size()) {
            bool found = false;
            while (r+1 < prices.size() && prices[r] <= prices[r+1]) {
                r++;
                found = true;
            }
            if (found) {
                if (prices[r] >= prices[r-1]) {
                    res += prices[r] - prices[l];
                } else {
                    res += prices[r-1] - prices[l];
                }
                l = r;
                r++;
            } else {
                res += prices[r] - prices[l];
                l = ++r;
                r++;
            }
            while (r < prices.size() && prices[l] >= prices[r]) {
                l++;
                r++;
            } 
            cout << res << endl;
        }
        return res;
    }
};