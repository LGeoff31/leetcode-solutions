class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> a;
        for (int i = 0; i < pow(2, nums.size()); i++) {
            vector<int> x;
            for (int j = 0; j < nums.size(); j++) {
                if ((1 << j) & i) {
                    x.push_back(nums[j]);
                }
            }
            a.push_back(x);
        }
        return a;
    }
};