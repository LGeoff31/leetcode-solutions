class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> seen;
        int res = 0;
        for (int i = 0; i < dominoes.size(); i++) {
            int a = min(dominoes[i][0],dominoes[i][1]);
            int b = max(dominoes[i][0], dominoes[i][1]);
            int key = 10*a+b;
            res += seen[key];
            seen[key]++;
            cout << res << endl;
        }
        return res;
    }
};