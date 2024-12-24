class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        vector<int> lst;
        for (int i = nums.size() - k; i < nums.size(); i++) {
            lst.push_back(nums[i]);
        }
        for (int i = 0; i < nums.size() - k; i++) {
            lst.push_back(nums[i]);
        }
        for (int i = 0; i < nums.size(); i++) {
            nums[i] = lst[i];
        }
    }
};