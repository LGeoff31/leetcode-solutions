class Solution {
public:
    int possibleStringCount(string word) {
        int cnt = 1;
        int res = 0;
        for (int i = 1; i < word.size(); i++) {
            if (word[i] == word[i-1]) {
                cnt++;
            } else {
                res += cnt - 1;
                cnt = 1;
            }
        }
        if (cnt > 1) res += cnt-1;
        return res + 1;
    }
};