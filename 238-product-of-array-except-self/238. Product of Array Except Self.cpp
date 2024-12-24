class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        int curr = 1;
        for (int num: nums) {
            curr *= num;
            prefix.push_back(curr);
        }
        curr = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            curr *= nums[i];
            suffix.push_back(curr);
        }
        reverse(suffix.begin(), suffix.end());
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) result.push_back(suffix[i+1]);
            else if (i == nums.size() - 1) result.push_back(prefix[i-1]);
            else result.push_back(prefix[i-1] * suffix[i+1]);
        }
        return result;

    }
};