class Solution {
public:
    bool isValid(int t, vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        if (grid[0][0] > t) return false;
        q.push(pair<int, int>{0, 0});
        vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int v[50][50]; // 1 -> visited
        memset(v, 0, sizeof(v)); // since v is on heap, has garbage values, so we use memset to set all bits to 0
        v[0][0] = 1;
        while (!q.empty()) {
            auto elem = q.front();
            int r = elem.first, c = elem.second;
            q.pop();
            if (r == grid.size() - 1 && c == grid[0].size() - 1) return true;
            for (auto [dr, dc] : dir){
                int new_r = r+dr, new_c = c+dc;
                if (0 <= new_r && new_r < grid.size() && 0 <= new_c && new_c < grid[0].size() && v[new_r][new_c]==0 && grid[new_r][new_c] <= t) {
                    v[new_r][new_c] = 1;
                    q.push(pair<int, int>{new_r, new_c});
                }
            }    
        }
        return false;
    }
    int swimInWater(vector<vector<int>>& grid) {
        int l = 0;
        int r = 0;
        for (int _r = 0; _r < grid.size(); _r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                r = max(r, grid[_r][c]);
            }
        }
        while (l <= r) {
            int mid = (l + r) / 2;
            if (isValid(mid, grid)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return r+1;
    }
};