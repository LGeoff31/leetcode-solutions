class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int n = security.size();
        if (time == 0) {
            vector<int> ans;
            for (int i=0; i<n; i++) ans.push_back(i);
            return ans;
        }
        vector<bool> dec(n, false), inc(n, false);
        int decIdx = 0, incIdx = n-1;
        for (int i=1; i<n; i++) {
            if (security[i] <= security[i-1]) {
                if (i - decIdx >= time) dec[i] = true;
            }
            else {
                decIdx = i;
            }
        }
        for (int i=n-2; i>=0; i--) {
            if (security[i] <= security[i+1]) {
                if (incIdx - i >= time) inc[i] = true;
            }
            else {
                incIdx = i;
            }
        }
        vector<int> ans;
        for (int i=0; i<n; i++) {
            if (dec[i] && inc[i]) ans.push_back(i);
        }
        return ans;
    }
};