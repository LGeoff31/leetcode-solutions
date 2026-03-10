class Solution {
public:
    struct KeyHash {
        size_t operator()(const tuple<int,int>& key) const {
            auto [a,b] = key;
            return hash<int>()(a) ^ (hash<int>()(b) << 1);
        } 
    };

    vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0,1}, {0,-1}};
    unordered_map<tuple<int, int>, int, KeyHash> memo;
    int dfs(int r, int c, vector<vector<int>>& matrix, int rows, int cols) {
        if (memo.count({r,c})) return memo[{r,c}];
        int res = 0;
        for (auto [dr, dc] : dir) {
            int new_r = r + dr;
            int new_c = c + dc;
            if (0 <= new_r && new_r < rows && 0 <= new_c && new_c < cols && matrix[new_r][new_c] > matrix[r][c]) {
            res = max(res, 1 + dfs(new_r, new_c, matrix, rows, cols));
            }
        }
        memo[{r,c}] = res;
        return res;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.size() == 1 && matrix[0].size() == 1) return 1;
        int res = 0;
        for (size_t r = 0; r < matrix.size(); r++) {
            for (size_t c = 0; c < matrix[0].size(); c++) {
            res = max(res, dfs(r, c, matrix, matrix.size(), matrix[0].size()));
            }
        }
        return res + 1;
    }
};