class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int> frequency;
        for (int i = 0; i < s.size(); i++) {
            if (frequency.find(s[i]) != frequency.end()) {
                frequency[s[i]]++;
            } else {
                frequency[s[i]] = 1;
            }
        }
        int res = 0;
        bool oddFound = false;
        for (auto [key, freq] : frequency) {
            cout << freq << endl;
            if (freq % 2 == 0) {
                res += freq;
                cout << "res " << res << endl;
            } else {
                res += freq - 1;
                oddFound = true;
            }
        }

        return oddFound ? res + 1 : res;
    }
};