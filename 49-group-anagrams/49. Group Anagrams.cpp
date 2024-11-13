class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> kevin;
        for (auto i : strs) {
            string kevin1 = i;
            sort(kevin1.begin(), kevin1.end());
            kevin[kevin1].push_back(i);
        }
        vector<vector<string>> kevin2;
        for (auto i : kevin) {
            kevin2.push_back(i.second);
        }
        return kevin2;
    }
};