class Solution {
public:
    int minF(string s) {
        int a = 0, b = 0;
        bool zero = true;
        // 010101
        for (int i = 0; i < s.size(); i++) {
            if (zero && s[i] == '1') a++;
            if (!zero && s[i] == '0') a++;
            zero = !zero;
        }
        // 10101
        zero = false;
        for (int i = 0; i < s.size(); i++) {
            if (zero && s[i] == '1') b++;
            if (!zero && s[i] == '0') b++;
            zero = !zero;
        }
        return min(a,b);
    }
    int minFlips(string s) {
        // 10101100101000000
        if (s.size() % 2 == 0 || s.size() == 1) return minF(s);
        int zeros_even_indicies = 0, ones_odd_indicies = 0;
        int total_zeros = count(s.begin(), s.end(), '0'), total_ones = count(s.begin(), s.end(), '1');

        for (int i = 0; i < s.size(); i++) {
            if (i % 2 == 0) {
                if (s[i] == '0') zeros_even_indicies++;
            } else {
                if (s[i] == '1') ones_odd_indicies++;
            }
        }
        int res = INT_MAX;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            // simulate n-1 swaps
            // 0101010101
            int expected_zeros = (n+1)/2;
            int expected_ones = n/2;
            res = min(res, expected_zeros - zeros_even_indicies + expected_ones - ones_odd_indicies);
            // 1010101011
            expected_zeros = n/2;
            expected_ones = (n+1)/2;
            res = min(res, zeros_even_indicies + ones_odd_indicies);
            int temp = ones_odd_indicies;
            char c = s[i];
            ones_odd_indicies = n/2 - zeros_even_indicies + (c == '0');
            zeros_even_indicies = (n+1)/2 - temp - (c == '1');
        }
        return res;
    }
};