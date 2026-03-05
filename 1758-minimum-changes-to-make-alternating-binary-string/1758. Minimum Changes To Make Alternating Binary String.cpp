class Solution {
public:
    int minOperations(string s) {
        // start 0
        int a = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i%2 == 0) {
                a += s[i] != '0';
            } else {
                a += s[i] != '1';
            }
        }
        // start 1
        int b = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i%2 == 0) {
                b += s[i] != '1';
            } else {
                b += s[i] != '0';
            }
        }

        return min(a,b);
    }
};