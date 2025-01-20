class Solution {
public:
    int findBlackPixel(vector<vector<char>>& picture, int target) {
        int m = picture.size(), n = picture[0].size(); 
        vector<string> keys; 
        unordered_map<string, int> freq; 
        vector<int> rows(m, 0), cols(n, 0); 
        for (int i = 0; i < m; ++i) {
            string key; 
            for (int j = 0; j < n; ++j) {
                key.push_back(picture[i][j]); 
                if (picture[i][j] == 'B') {
                    ++rows[i]; 
                    ++cols[j]; 
                }
            }
            keys.push_back(key); 
            ++freq[key]; 
        }
        
        int ans = 0; 
        for (int i = 0; i < m; ++i) {
            string key = keys[i]; 
            if (freq[key] == target) 
                for (int j = 0; j < n; ++j) 
                    if (picture[i][j] == 'B' && rows[i] == target && cols[j] == target) 
                        ++ans; 
        }
        return ans; 
    }
};