class Solution {
public:
    string makeFancyString(string s) {
        string res = "";
        res+=s[0];
        int curr = 1;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i-1]) {
                curr++;
                if (curr < 3) {
                    res += s[i];
                }
            } else {
                curr = 1;
                res += s[i];
            }
        }
        return res;
    }
};