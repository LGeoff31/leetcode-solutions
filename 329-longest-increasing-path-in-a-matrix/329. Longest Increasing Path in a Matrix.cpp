class Solution {
public:
    struct KeyHash {
        size_t operator()(const tuple<int,int,int>& key) const {
            auto [a,b,c] = key;
            return hash<int>()(a) ^ (hash<int>()(b) << 1) ^ (hash<int>()(c) << 2);
        }
    };
    vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0,1}, {0,-1}};
    unordered_map<tuple<int, int, int>, int, KeyHash> memo;
    int dfs(int r, int c, int prevVal, vector<vector<int>>& matrix, int rows, int cols) {
        int res = 0;
        if (memo.count({r,c,prevVal})) return memo[{r,c,prevVal}];
        for (auto [dr, dc] : dir) {
            int new_r = r + dr;
            int new_c = c + dc;
            if (0 <= new_r && new_r < rows && 0 <= new_c && new_c < cols && matrix[new_r][new_c] > prevVal) {
            res = max(res, 1 + dfs(new_r, new_c, matrix[new_r][new_c], matrix, rows, cols));
            }
        }
        memo[{r,c,prevVal}] = res;
        return res;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.size() == 1 && matrix[0].size() == 1) return 1;
        int res = 0;
        for (size_t r = 0; r < matrix.size(); r++) {
            for (size_t c = 0; c < matrix[0].size(); c++) {
            res = max(res, dfs(r, c, -1, matrix, matrix.size(), matrix[0].size()));
            }
        }
        
        return res;
    }
};