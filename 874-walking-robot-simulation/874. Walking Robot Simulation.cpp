class Solution {
public:
    struct pair_hash {
        size_t operator()(const pair<int, int>& p) const {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<pair<int, int>, pair_hash> obstacles_set;
        vector<string> directions = {"N", "R", "S", "L"};
        int idx = 0;
        for (auto pair : obstacles) {
            obstacles_set.insert({pair[0], pair[1]});
        }
        int x = 0, y = 0;
        int res = 0;
        for (auto c : commands) {
            if (c == -2) {
                idx = (idx -1);
                if (idx == -1) idx = 3;
            } else if (c == -1) {
                idx = (idx + 1) % 4;
            } else {
                for (int i = 0; i < c; i++) {
                    cout << x << y << endl;
                    if (directions[idx] == "N") {
                        if (obstacles_set.count({x,y+1})) break;
                        y++;
                    } 
                    if (directions[idx] == "S") {
                        if (obstacles_set.count({x,y-1})) break;
                        y--;
                    } 
                    if (directions[idx] == "L") {
                        if (obstacles_set.count({x-1,y})) break;
                        x--;
                    } 
                    if (directions[idx] == "R") {
                        if (obstacles_set.count({x+1,y})) break;
                        x++;
                    } 
                    cout << x << y << endl;
                    res = max(res, x*x+y*y);
                }
            }
        }
        return res;
    }
};