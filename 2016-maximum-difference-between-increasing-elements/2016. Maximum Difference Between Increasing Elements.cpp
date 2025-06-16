class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int res = -1;
        int min_element = INT_MAX;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > min_element) {
                res = max(res, nums[i] - min_element);
            }
            min_element = min(min_element, nums[i]);
        }
        return res;
    }
};