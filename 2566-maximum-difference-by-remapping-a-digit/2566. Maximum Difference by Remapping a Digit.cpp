class Solution {
public:
    int minMaxDifference(int num) {
        string s = to_string(num);
        int minVal = INT_MAX, maxVal = 0;
        for (char c1 = '0'; c1 <= '9'; c1++) {
            for (char c2 = '0'; c2 <= '9'; c2++) {
                string t = s;
                for (auto& c : t) {
                    if (c == c1) {
                        c = c2;
                    }
                }
                int val = stoi(t);
                cout << val << endl;
                minVal = min(minVal, val);
                maxVal = max(maxVal, val);
            }
        }
        return maxVal - minVal;
    }
};