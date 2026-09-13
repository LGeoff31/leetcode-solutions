class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();

        vector<pair<int, int>> pos1;
        vector<pair<int, int>> pos2;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(img1[i][j] == 1) {
                    pos1.push_back({i, j});
                }

                if(img2[i][j] == 1) {
                    pos2.push_back({i, j});
                }
            }
        }

        int res = 0;
        map<pair<int, int>, int> mp;

        for(auto p1 : pos1) {
            for(auto p2 : pos2) {
                int r = p2.first - p1.first;
                int c = p2.second - p1.second;

                mp[{r, c}]++;

                res = max(res, mp[{r, c}]);
            }
        }

        return res;
    }
};