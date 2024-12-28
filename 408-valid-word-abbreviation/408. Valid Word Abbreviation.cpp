class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int i = 0, j = 0;
        while (i < word.length() && j < abbr.length()) {
            cout << word[i] << endl;
            cout << abbr[j] << endl;
            if (isdigit(abbr[j])) {
                // Extract out the entire number
                string num = "";
                while (j < abbr.length() && isdigit(abbr[j])) {
                    num += abbr[j];
                    j++;
                }
                cout << num << endl;
                int val = stoi(num);
                if (num[0] == '0') return false;
                i += val;
            } else {
                if (abbr[j] == word[i]) {
                    i++;
                    j++;
                } else {
                    return false;
                }
            }
        }
        // cout << i << " " << j << endl;
        // cout << word.length() << " " << abbr.length() << endl;
        return i == word.length() && abbr.length() == j;
    }
};